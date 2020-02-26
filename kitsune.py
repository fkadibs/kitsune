import xml.etree.ElementTree as ET
from fontTools.ttLib import TTFont
from string import ascii_letters
from random import shuffle
import sys
import os

if len(sys.argv) < 2:
    exit('Usage: font-cipher.py <filename> [text]')

extension = sys.argv[1].split('.')[-1]

# generate random substitutions
normal = [l for l in ascii_letters]
rand = [l for l in ascii_letters]
shuffle(rand) # modify in place
subs = { x: y for x, y in zip(normal, rand)}

if extension == 'ttf':
    # convert source to xml
    print('[+] Loading file...')
    font = TTFont(sys.argv[1])
    font.saveXML('output.ttx')

    # apply the substitutions
    print('[+] Applying substitutions...')
    font_tree = ET.parse('output.ttx')
    font_root = font_tree.getroot()
    for letter in font_root.iter('map'):
        if letter.attrib['name'] in subs.keys():
            letter.set('name', subs[letter.attrib['name']])
    font_tree.write('output.ttx')

    # convert to ttf
    print('[+] Writing to disk...')
    font = TTFont()
    font.importXML('output.ttx')
    font.save('output.ttf')

elif extension == 'ttx':
    # load the xml
    font_root = ET.parse(sys.argv[1]).getroot()
    for letter in font_root.iter('map'):
        if letter.attrib['name'] in normal:
            # reverse map keys by cmap hex code
            subs[chr(int(''.join(letter.attrib['code'][-2::]), 16))] = letter.attrib['name']

if len(sys.argv) > 2:
    print('\n' + ''.join(subs[l] if l in subs.keys() else l for l in sys.argv[2]))
