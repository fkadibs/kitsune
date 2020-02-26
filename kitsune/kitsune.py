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
shuffle(rand)
subs = { x: y for x, y in zip(normal, rand)}

def main():
    if extension == 'ttf':
        # convert source to xml
        print('[+] Loading source font...')
        font = TTFont(sys.argv[1])
        print('[+] Generating .ttx file...')
        font.saveXML('output.ttx')
        # prase xml
        font_tree = ET.parse('output.ttx')
        font_root = font_tree.getroot()
        for letter in font_root.iter('map'):
            if letter.attrib['name'] in subs.keys():
                letter.set('name', subs[letter.attrib['name']])
        font_tree.write('output.ttx')

        # convert to ttf
        print('[+] Generating .ttf file...')
        font = TTFont()
        font.importXML('output.ttx')
        font.save('output.ttf')

    elif extension == 'ttx':
        # load the xml
        font_root = ET.parse(sys.argv[1]).getroot()
        for letter in font_root.iter('map'):
            if letter.attrib['name'] in normal:
                # reverse map with hex key
                subs[chr(int(''.join(letter.attrib['code'][-2::]), 16))] = letter.attrib['name']

    if len(sys.argv) > 2:
        print('\n' + ''.join(subs[l] if l in subs.keys() else l for l in sys.argv[2]))

if __name__ == '__main__':
    main()
