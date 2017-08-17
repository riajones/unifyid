import math
import os.path
from PIL import Image
from get_numbers import request


def create_image(download=True):
	size = 128
	rgb_vals = []
	if download or not os.path.isfile('bits.txt'):
		rgb_vals = request(math.pow(size,2) * 3)
		# cache last downloaded values to save time and load on random.org
		open('bits.txt', 'w').write(rgb_vals)
	else:
		# Load last downloaded vals
		rgb_vals = open('bits.txt').read()
		import re
		rgb_vals = re.sub(r' |\[|\]', '', rgb_vals)
		rgb_vals = list(map(int, rgb_vals.split(',')))

	im = Image.new("RGB", (size,size))
	pixels = []
	for i in range(size * size):
		r = rgb_vals[i]
		g = rgb_vals[i + 1]
		b = rgb_vals[i + 2]
		pixels.append((r, g, b))
		i += 2

	im.putdata(pixels)
	im.save('image.bmp')



create_image(False)