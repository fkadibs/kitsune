import xml.etree.ElementTree as ET	
from fontTools.ttLib import TTFont, woff2
from string import ascii_letters	
from random import shuffle	
import argparse
import sys	
import os

parser = argparse.ArgumentParser()
parser.add_argument('filename', action='store', help='input filename')
parser.add_argument('-c', action='store', metavar='TEXT', help='generate ciphertext')
parser.add_argument('-o', action='store', metavar='FILE', default='output', help='output file name')
args = parser.parse_args()

EXT = args.filename.split('.')[-1]
OUT_TTX, OUT_TTF = (args.o + i for i in ['.ttx', '.ttf'])

# generate random substitutions	
normal = [l for l in ascii_letters]	
rand = [l for l in ascii_letters]	
shuffle(rand) # modify in place	
subs = { y: x for x, y in zip(normal, rand) }	

def main():
    if EXT == 'ttf':	
        # convert source to xml	
        print('[+] Loading {}..'.format(args.filename))
        font = TTFont(args.filename)	
        font.saveXML(OUT_TTX)	
        
        # parsing XML
        print('[+] Generating {} file...'.format(OUT_TTX))
        font_tree = ET.parse(OUT_TTX)	
        font_root = font_tree.getroot()

        for letter in font_root.iter('map'):	
            if letter.attrib['name'] in subs.keys():
                letter.set('code', hex(ord(subs[letter.attrib['name']])))
        
        font_tree.write(OUT_TTX)	

        # convert to ttf	
        print('[+] Generating {} file...'.format(OUT_TTF))	
        font = TTFont()	
        font.importXML(OUT_TTX)	
        font.save(OUT_TTF)

    elif EXT == 'ttx':	
        # load the xml	
        font_root = ET.parse(args.filename).getroot()
        for l in normal:
            for letter in font_root.iter('map'):
                if letter.attrib['code'] == hex(ord(l)):
                    subs[letter.attrib['name']] = l

    if args.c:	
        print('\n' + ''.join(subs[l] if l in subs.keys() else l for l in args.c))


if __name__ == '__main__':
    main()
