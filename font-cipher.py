import xml.etree.ElementTree as ET
from fontTools.ttLib import TTFont
from string import ascii_letters
from random import shuffle
import sys
import os

if len(sys.argv) < 2:
    exit('Usage: font-cipher.py <filename> [text]')

# generate random substitutions
normal = [l for l in ascii_letters]
rand = [l for l in ascii_letters]
shuffle(rand) # modify in place
subs = { x: y for x, y in zip(normal, rand) }

# convert source to xml
print('[+] Loading file...')
font = TTFont(sys.argv[1])
font.saveXML('tmp.xml')

# apply the substitutions
print('[+] Applying substitutions...')
font_tree = ET.parse('tmp.xml')
font_root = font_tree.getroot()
for letter in font_root.iter('map'):
    if letter.attrib['name'] in subs.keys():
        letter.set('name', subs[letter.attrib['name']])
font_tree.write('tmp.xml')

# convert to ttf
print('[+] Writing to disk...')
font = TTFont()
font.importXML('tmp.xml')
font.save('output.ttf')

# cleanup
os.remove('tmp.xml')

if len(sys.argv) > 2:
    print('[+] Ciphertext:')
    output_string = ''.join(subs[l] if l in subs.keys() else l for l in sys.argv[2])
    print(output_string)
