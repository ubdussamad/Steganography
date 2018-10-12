#!/usr/bin/env python3

'''-------------------------------------------------------------
* Pixel Wise Image Analyzer cum Decrypter
* (Recovers data embedded in an image.)
* 07OCT2018
* Authors: Mohammed S. Haque <ubdussamad@gmail.com>
* Primarily Built around Python3.x

* Usage:
* user@machine~$ ./dec.py
* It'll automatically save the decrypted data as an extension-less file named: recovered_data
*
* This program currently utilizes an even odd scheme to store/read binary data into/from an image.
*
* Working Principle:
* Reads a Portable Network Graphic (.png) by converting it to a 2D array.
* An odd color value represents binary 0 and an even color value represents binary 1.
* Primarily color values in the image's matrix are converted into odd integer by adding
* integer value 1 if the color value is even else 0 if the color value is already odd.
------------------------------------------------------------------------------------------'''

from PIL import Image
import numpy as np
import time,math
img = Image.open('secret.png') #Reading the Image
arr = np.array(img) #Converting the Image into a 2D array
x,y,z  = np.shape(arr) #Reading the dimensions of the array to determine the storage.
arr = arr.ravel() & 1 #Converting every value in the matrix to 0 if it's even else 1.
data_array = arr ^ 1 #Noting every value in the matrix.
reserved_bit_width =  math.ceil(math.log2((x*y*3)/8))
print("The dimensions of the image are: %dx%dx%d pixels."%(x,y,z))
data_bytes = int(''.join(map(str , data_array[:reserved_bit_width])),2)
print("The enclosed data is of size: %d Bytes"%(data_bytes))
data_array = data_array[ reserved_bit_width : (data_bytes * 8) + reserved_bit_width]
data_array = bytearray(np.packbits(data_array))
print("Start byte:%d / Mid byte: %d / End Byte:%d"%(data_array[0],data_array[1],data_array[-1]))
with open('recovered_data','wb') as f_obj:
	f_obj.write(data_array)
print('_'*45,"\nEnclosed data saved as: recovered_data")
