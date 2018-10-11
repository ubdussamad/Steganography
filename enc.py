#!/usr/bin/env python3
from PIL import Image
import numpy as np
import time,math


img = Image.open('Desktop/test.jpg') #Reading the Image
arr = np.array(img) #Converting the Image into a 2D array
x,y,z  = np.shape(arr) #Reading the dimensions of the array to determine the storage.
arr |= 1 #Making every value in the matrix odd

print("The amount of data you can store in this image is: %d kiBs"%((x*y*z)/(1024*8)))

reserved_bit_width =  math.ceil(math.log2((x*y*3)/8))

path_string = 'test.jpg'#input("Enter the path:") # Scanning the string to be stored.

long_array = [] #Array containing the binary values.

with open(path_string,'rb') as f_obj:
	tmp = f_obj.read()
	f_obj.close()

string = ''

print("performing string stuff.")
for i in tmp:
	string += "%s,"%str(i)

print("Done with  string stuff")

long_array = [] #Array containing the binary values.

for i in string:
    long_array += list(map(int,list(format(ord(i), '#010b')[2:]))) #Storing the characters in binary form (ASCII)

#long_array = np.array([int(i) for i in ''.join([bin(int(format(ord(i), '#010b'),2))[2:] for i in z])])

arr.ravel()[:len(long_array)] += np.array(long_array, arr.dtype) #Adds one if there is a one else adds zero hence making even odd pairs. 

image = Image.fromarray(arr) #Recreating the image from the modified array.

image.show() #Displaying the picture.

image.save("secret.png") #Saving the Image for transfer or future use. Note: The output picture must be in PNG format
#As other formats try to compress the data corrupting the encoded data within the image.
