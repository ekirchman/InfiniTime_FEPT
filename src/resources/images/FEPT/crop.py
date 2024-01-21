from PIL import Image
import argparse
import os

parser = argparse.ArgumentParser(
                    prog='P2RGBA',
                    description='Crops image of Lyn')
parser.add_argument('-filename', '-f', help='Crops', required=True)           # positional argument
args = parser.parse_args()

img = Image.open(args.filename)

cropped = img.crop((100, 77, 120, 112))

newW, newH = cropped.size
newW = newW * 2
newH = newH * 2

scaled = cropped.resize((newW, newH), Image.Resampling.NEAREST)
# scaled.show()
scaled.save(args.filename)
