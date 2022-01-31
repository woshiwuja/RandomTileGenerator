import numpy as np
from PIL import Image, ImageColor
from numpy import random
import base64
HEIGHT = 16
WIDTH = 16 
r = 255
g = 255
b = 255

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
inputTextH = input("Insert height:")
inputTextW = input("Insert width:")
inputTextImageName = input("Insert new file name + extension:")
HEIGHT = int(inputTextH)
WIDTH = int(inputTextW)
img = Image.new('RGB', (HEIGHT,WIDTH)) # create the Image of size Height*Width pixel 
for i in range(WIDTH):
	r = create_red_from_base(rgb[0])
	g = create_green_from_base(rgb[1])
	b = create_blue_from_base(rgb[2])
	for j in range (HEIGHT):
		r = create_red_from_base(rgb[0])
		g = create_green_from_base(rgb[1])
		b = create_blue_from_base(rgb[2])
		img.putpixel((j,i),(r,g,b))
	img.putpixel((j,i),(r,g,b))
img.save(inputTextImageName) # or any image format
with open(inputTextImageName, "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read())
