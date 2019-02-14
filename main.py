#!/usr/bin/env python3

import os
import sys
import argparse

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


size = 400
available_formats = ['PNG']
available_colors = ['green', 'blue', 'black', 'yellow', 'white']


def create_image(size, color, letter):
	"""
	Create PIL image
	"""
	img = Image.new('RGB', (size, size), color)
	draw = ImageDraw.Draw(img)
	fnt = ImageFont.truetype('OpenSans-Light.ttf', 200)
	draw.text((size / 3, size / 8), letter, font=fnt, fill=(255, 255, 255, 255))
	return img


def main():
	parser = argparse.ArgumentParser(description='Color Letter Images')
	parser.add_argument('-l', '--letter', help='Output image letter', required=True)
	parser.add_argument('-b', '--background', help='Output image backgroud', required=True)
	parser.add_argument('-o', '--output', help='Output image file name', required=True)
	args = parser.parse_args()

	# Check letter length
	if len(args.letter) > 1:
		text = 'error: length -l can not be longer 1'
		print(text)
		sys.exit(1)
	parse_file = os.path.splitext(args.output)
	# Check output file extension
	if len(parse_file) <= 1:
		text = 'error: no file extension'
		print(text)
		sys.exit(1)
	# Check extension format
	if parse_file[1][1:].upper() not in available_formats:
		text = 'error: file has not available format\n\nAvailable formats:'
		for x in available_formats:
			text += '\n' + x
		print(text)
		sys.exit(1)
	# Check background color
	if args.background not in available_colors:
		text = 'error: background has not available color\n\nAvailable colors:'
		for x in available_colors:
			text += '\n' + x
		print(text)
		sys.exit(1)

	letter = args.letter
	background = args.background
	output = args.output
	file_extension = parse_file[1][1:].upper()

	img = create_image(size, background, letter)
	img.save(output, file_extension)
	print('Image <{!s}> successfully created!'.format(output))


if __name__ == '__main__':
	main()
