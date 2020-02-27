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
parser.add_argument('-w', action='store_true', help='generate woff2 webfont')
args = parser.parse_args()

extension = args.filename.split('.')[-1]

# generate random substitutions	
normal = [l for l in ascii_letters]	
rand = [l for l in ascii_letters]	
shuffle(rand) # modify in place	
subs = { x: y for x, y in zip(normal, rand)}	

def main():
    if extension == 'ttf':	
        # convert source to xml	
        print('[+] Loading file...')	
        font = TTFont(args.filename)	
        font.saveXML(args.o + '.ttx')	

        # apply the substitutions	
        print('[+] Applying substitutions...')	
        font_tree = ET.parse(args.o + '.ttx')	
        font_root = font_tree.getroot()	
        for letter in font_root.iter('map'):	
            if letter.attrib['name'] in subs.keys():	
                letter.set('name', subs[letter.attrib['name']])	
        font_tree.write(args.o + '.ttx')	

        # convert to ttf	
        print('[+] Writing to disk...')	
        font = TTFont()	
        font.importXML(args.o + '.ttx')	
        font.save(args.o + '.ttf')

        if args.w:
            woff2.compress(input_file=args.o +'.ttf', output_file=args.o + '.woff2')

    elif extension == 'ttx':	
        # load the xml	
        font_root = ET.parse(args.filename).getroot()	
        for letter in font_root.iter('map'):	
            if letter.attrib['name'] in normal:	
                # reverse map keys by cmap hex code
                hex_code = ''.join(letter.attrib['code'][-2::])
                ascii_key = chr(int(hex_code, 16))
                subs[ascii_key] = letter.attrib['name']

    if args.c:	
        print('\n' + ''.join(subs[l] if l in subs.keys() else l for l in args.c))


if __name__ == '__main__':
    main()
