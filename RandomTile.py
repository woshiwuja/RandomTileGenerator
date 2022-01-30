import numpy as np
import png
from PIL import Image, ImageColor
from numpy import random
HEIGHT = 16 # 16 * 3
WIDTH = 16 
#TILE = np.empty(shape=(WIDTH,HEIGHT), dtype=Uint8ClampedArray)
PIXEL = np.zeros([1,3],dtype=object)
r = 0
g = 0
b = 0
def create_red_channel(r):
	r = random.randint(20,100)
	return r
def create_green_channel(g):
	g = random.randint(50,125)
	return g
def create_blue_channel(b):
	b = random.randint(50,200)
	return b
def create_random_pixel(r,g,b):
	r = 0
	g = 0
	b = 0
	r = create_red_channel(r)
	g = create_green_channel(g)
	b = create_blue_channel(b)
	PIXEL = ([r,g,b])
	return PIXEL

img = Image.new('RGB', (16,16)) # create the Image of size 1 pixel 
for i in range(16):
	r = create_red_channel(r)
	g = create_green_channel(g)
	b = create_blue_channel(b)
	for j in range (16):
		r = create_red_channel(r)
		g = create_green_channel(g)
		b = create_blue_channel(b)
		img.putpixel((j,i),(r,g,b))
img.putpixel((j,i),(r,g,b))

img.save('simplePixel.png') # or any image format
