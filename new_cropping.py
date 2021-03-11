#ipmorting libraries
import cv2 as cv
from PIL import Image
import numpy as np

#example coordinates of a square
#top left, bottom left, bottom right, top right
x = [20, 20, 40, 40]
y = [20, 40, 40, 20]

#the following is stack overflow code to make a matrix of a bunch of zeroes and
#a square of ones which we designated by the two lists above
contours = np.stack((x, y), axis = 1)
polygon = np.array([contours], dtype = np.int32)
zero_mask = np.zeros((100, 100), np.uint8)
polyMask = cv.fillPoly(zero_mask, polygon, 1)

#a dictionary of the start and end coordinates
coordinates = dict()
first_one = False

#iterating through the mask matrix
for i in range(len(polyMask)):
    
    for j in range(len(polyMask[i])):

        #if we've reached the first one, then we can keep track of it in the coordinates dictionary
        if polyMask[i][j] == 1 and first_one == False:
            coordinates['start'] = (i, j)
            first_one = True
        
        #keep overwriting the end entry to the coordinate dictionary everytime we see a 1; eventually we will
        #reach the lsat 1 in the mask
        if polyMask[i][j] == 1 and first_one == True:
            coordinates['end'] = (i, j)

print(coordinates)

#print(polyMask)
#cv.imwrite("newimage.png", polyMask)