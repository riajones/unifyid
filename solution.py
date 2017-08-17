import math
import struct
import os.path
import wave
from PIL import Image
from get_numbers import request


def create_image(download=True):
	size = 128
	rgb_vals = []
	if download or not os.path.isfile('bits.txt'):
		rgb_vals = request(math.pow(size,2) * 3)
		# cache last downloaded values to save time and load on random.org
		open('bits.txt', 'w').write(str(rgb_vals))
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

def create_wav(download=True):
	length = 3
	# Note that I had to use a very low sample rate to get around the bit quota on random.org
	# sample_rate = 44100
	sample_rate = 320
	wav_max = 32767


	values = []
	if download or not os.path.isfile('noise.txt'):
		values = request(length * sample_rate, wav_max * -1, wav_max)
		# cache last downloaded values to save time and load on random.org
		open('noise.txt', 'w').write(str(values))
	else:
		# Load last downloaded vals
		values = open('noise.txt').read()
		import re
		values = re.sub(r' |\[|\]', '', values)
		values = list(map(int, values.split(',')))


	out = wave.open('sound.wav', 'w')
	out.setparams((2, 2, sample_rate, 0, 'NONE', 'not compressed'))

	for val in values:
		out.writeframesraw(struct.pack('<hh', val, val ))
	out.close()


create_image()
create_wav()