#!/bin/python
import collections, functools, operator
from new_cropping import *
from PIL import Image
from tqdm import tqdm 
import os

def make_test(m, n, a, b, color=1):
	
	x = [a, a, b, b]
	y = [a, b, b, a]

	contours = np.stack((x, y), axis = 1)
	polygon = np.array([contours], dtype = np.int32)
	zero_mask = np.zeros((m, n), np.uint8)
	polyMask = cv.fillPoly(zero_mask, polygon, color)
	
	return polyMask
	
# height, width
# example:
# matrix = make_test(850, 1000, 200, 400)

def assert_dimensions(output_img, n):
	
	img_path = os.path.abspath(output_img)
	image = Image.open(img_path)
	shape = image.size
	image.close()
	size_right = False
	if shape[0] == n and shape[1] == n:
		size_right = True
		
		print("Success: Output file", output_img, "has the correct dimensions")
		
	elif size_right == False:
		print("Error: Output file", output_img, "has incorrect dimensions")
		
# example demo

file = "S8840_Before_V1.jpg"
cropped_file = file[:-4] + "_cropped.jpg"
cd = "."

petrous = mask_from_file(cd, file, "./JSON_annotations/petrous_kushal.json", cd)

# find the desired dimensions for the cropped image size, default is 1000
n = n_finder(petrous)

cropper(cd, file, petrous, n)	

assert_dimensions(file, n)
# should print out an error, it's the image before cropping
assert_dimensions(cropped_file, n)
# should print out success, using the cropped image as input





