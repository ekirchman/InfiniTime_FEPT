from PIL import Image
import argparse
import os
parser = argparse.ArgumentParser(
                    prog='P2RGBA',
                    description='Converts 8-bit "pixel" image formats to RGBA')
parser.add_argument('-filename', '-f', help='8-bit Pixel image to be formated to RGBA', required=True)           # positional argument
args = parser.parse_args()

img = Image.open(args.filename)

if(img.mode != 'P'):
    print(f"Image is not of type 'P'. It is a {img.mode} type")
else:
    img_RGBA = img.convert('RGBA')
    backup_filename = args.filename.split('.')[0] + "_P." + args.filename.split('.')[1]
    # print(backup_filename)
    os.rename(args.filename, backup_filename)
    img_RGBA.save(args.filename)
