import numpy as np
import png
from PIL import Image, ImageColor
from numpy import random
HEIGHT = 16
WIDTH = 16 
PIXEL = np.zeros([1,3],dtype=object)
r = 255
g = 255
b = 255

def create_random_red_channel(r):
	noise = random.randint(100)
	r = random.randint(10,70)
	if noise <= 10 and r<245:
		r += noise
	return r

def create_random_green_channel(g):
	noise = random.randint(100)
	g = random.randint(200,255)
	if noise <= 10 and g<245:
		g += noise
	return g

def create_random_blue_channel(b):
	noise = random.randint(100)
	b = random.randint(55,90)
	if noise <= 10 and b<245:
		b += noise
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

def create_red_from_base(r):
	noise = random.randint(100)
	if noise <= 20 and r<125:
		r += noise
	elif noise>=20 and r>=125:
		r -= noise
	return r
def create_green_from_base(g):
	noise = random.randint(100)
	if noise <= 50 and g<125:
		g += noise
	elif noise<=50 and g>=125:
		g -= noise
	return g

def create_blue_from_base(b):
	noise = random.randint(100)
	if noise <= 50 and b<125:
		b += noise
	elif noise<=50 and b>=125:
		b -= noise
	return b

rgb = []
inputTextR = input("Insert R:")
r = int(inputTextR)
rgb.append(r)
inputTextG = input("Insert G:")
g = int(inputTextG)
rgb.append(g)
inputTextB = input("Insert B:")
b = int(inputTextB)
rgb.append(b)

img = Image.new('RGB', (HEIGHT,WIDTH)) # create the Image of size Height*Width pixel 
for i in range(16):
	r = create_red_from_base(rgb[0])
	g = create_green_from_base(rgb[1])
	b = create_blue_from_base(rgb[2])
	print (r,g,b)
	for j in range (16):
		r = create_red_from_base(rgb[0])
		g = create_green_from_base(rgb[1])
		b = create_blue_from_base(rgb[2])
		img.putpixel((j,i),(r,g,b))
		print (r,g,b)
	img.putpixel((j,i),(r,g,b))
img.save('tile.png') # or any image format
