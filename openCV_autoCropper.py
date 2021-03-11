#!/usr/bin/python

import cv2
from PIL import Image
import os 

## file dictionary containing the names of the files in the image directory and the quadrant that you want to crop. Follows the convention top right = 1, top left = 2, bottom left = 3, bottom right = 4
fdict = {"RSIP_Example_HipSegmentation.jpg" : 1}

def autoCropper(image_dir, cropped_dir, file_dict):
	
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
		
		"""# if quadrant is specified as 1, do this type of cropping, and so on for all 4 quadrants
		if v == 1:
			crop_img = img[0:midy, midx:x]	
			
		elif v == 2: 
			crop_img = img[0:midy, 0:midx]
		
		elif v == 3: 
			crop_img = img[midy:y, 0:midx]
		
		elif v == 4: 
			crop_img = img[midy:y, midx:x]"""
			
		
		# Write the cropped image to a new file, specified the name using the full destination directory path and "_cropped.jpg" as suffix
		cv2.imwrite(cropped_fname, crop_img)
		
		return print(cropped_fname, "created successfully")
			

if __name__ == "__main__":
	crop = autoCropper("images_dir", "crop_dir", fdict)

