#!/usr/bin/env python3

'''-------------------------------------------------------------
* Pixel Wise Image Modification cum Encryption Utility.
* (Embeds String data into an image.)
* 07OCT2018
* Authors: Mohamed S. Haque <ubdussamad@gmail.com>
* Primarily Built around Python3.x
*
* Usage:
* user@machine~$ ./enc.py [path_to_image_which_will_store_data] [path_to_file_which_is_to_be_enclosed]
* The output Image will be saved as secret.png in the same directory as this file.
*
* This program currently utilizes an even odd scheme to store/read binary data into/from an image.
*
* Working Principle:
* Reads a Portable Network Graphic (.png) and converts it to a 2D array.
* An odd color value represents binary 0 and an even color value represents binary 1.
* Primarily color values in the image's matrix are converted into odd integer by adding
* integer value 1 if the color value is even else 0 if the color value is already odd.
*
* Scheme: Odd if 0 , even if 1
------------------------------------------------------------------------------------------'''


from PIL import Image
import numpy as np
import math,sys
storage_path,path_string = sys.argv[1:3]
arr = np.array(Image.open(storage_path)) #Converting the Image into a 2D array
x,y,z  = np.shape(arr) #Reading the dimensions of the array to determine the storage.
arr |= 1 #Making every value in the matrix odd
reserved_bit_width =  math.ceil(math.log2((x*y*3)/8))
with open(path_string,'rb') as f_obj:
	file_data = f_obj.read()

print("The amount of data you can store in this image is: %d KiBs"%((x*y*z)/(1024*8)))
print("The size of the file is: %d Bytes"%len(file_data))
print("Start byte:%d, Mid byte: %d End byte: %d"%(file_data[0],file_data[1] , file_data[-1]))

long_array = np.array([ int(i) for i in format(len(file_data) , '#0%db'%(reserved_bit_width+2) )[2:] ])
long_array = np.concatenate( ( long_array , np.unpackbits(bytearray(np.array(file_data))) ) , axis = 0 )
arr.ravel()[:len(long_array)] += np.array(long_array, arr.dtype) #Adds one if there is a one else adds zero hence making even odd pairs. 

print("Asserting Checks.")
assert( not(  (len(long_array) - reserved_bit_width )%8 ) )
print("Recreating the Image, Plese wait...\n")

image = Image.fromarray(arr) #Recreating the image from the modified array.
image.save("secret.png") #Saving the Image for transfer or future use. Note: The output picture must be in PNG format
#As other formats try to compress the data corrupting the encoded data within the image.
print('_'*50,"\nDone Rendering Image.")
