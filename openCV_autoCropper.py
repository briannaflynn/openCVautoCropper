#!/usr/bin/python

import cv2
from PIL import Image
import os 
import sys 

## file dictionary containing the names of the files in the image directory and the quadrant that you want to crop. Follows the convention top right = 1, top left = 2, bottom left = 3, bottom right = 4
# fdict = {"S8138_Before_V1.jpg" : 'center'}
image_dir = sys.argv[1]
crop_dir = sys.argv[2]

filedict = dict()
flist = []
for f in os.listdir(image_dir):
	j = {f: sys.argv[3]}
	flist.append(j)
print(flist)

def quadCropper(image_dir, cropped_dir, file_dict):
	
	# get the full paths of the input and destination directories
	full_path = os.path.abspath(image_dir)
	full_cropped_path = os.path.abspath(cropped_dir)
	
	# k is the filename, v is the quadrant	
	for k, v in file_dict.items():
		
		fname = full_path + "/" + k
		
		cropped_fname = full_cropped_path + "/" + k[:-4] + "_cropped.jpg"
		
		# get the dimensions of the image using PIL, returns a tuple with (x, y)		
		absolute_img_filename = fname		
		image = Image.open(absolute_img_filename)
		shape = image.size
		image.close()
		
		# get x and y dimensions, as well as midpoint coords	
		x = shape[0]
		y = shape[1]
		midx = x // 2
		midy = y // 2
		
		# read in the full input path to open cv2
		img = cv2.imread(fname)
		
		# if quadrant is specified as 1, do this type of cropping, and so on for all 4 quadrants
		if v == 1:
			crop_img = img[0:midy, midx:x]	
			
		elif v == 2: 
			crop_img = img[0:midy, 0:midx]
		
		elif v == 3: 
			crop_img = img[midy:y, 0:midx]
		
		elif v == 4: 
			crop_img = img[midy:y, midx:x]
			
		elif v == "center":
			n = 2
			mid_y_1 = midy - midy // n
			mid_y_2 = midy + midy // n
			mid_x_1 = midx - midx // n
			mid_x_2 = midx + midx // n
			crop_img = img[mid_y_1:mid_y_2, mid_x_1:mid_x_2]
			
		
		# Write the cropped image to a new file, specified the name using the full destination directory path and "_cropped.jpg" as suffix
		cv2.imwrite(cropped_fname, crop_img)
		
		return print(cropped_fname, "created successfully")
			

for l in flist:
	quadCropper(image_dir, crop_dir, l)