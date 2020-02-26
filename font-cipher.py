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
subs = [l for l in ascii_letters]
shuffle(subs)
cmap = { x: y for x, y in zip(normal, subs)}

# convert source to xml
font = TTFont(sys.argv[1])
font.saveXML('tmp.xml')

# apply the substitutions
font_tree = ET.parse('tmp.xml')
font_root = font_tree.getroot()
for code in font_root.iter('map'):
    if code.attrib['name'] in cmap.keys():
        code.set('name', cmap[code.attrib['name']])
font_tree.write('tmp.xml')

# convert to ttf
font = TTFont()
font.importXML('tmp.xml')
font.save('output.ttf')

# cleanup
os.remove('tmp.xml')

if len(sys.argv) > 2:
    output_string = ''.join(cmap[l] if l in cmap.keys() else l for l in sys.argv[2])
    print(output_string)
