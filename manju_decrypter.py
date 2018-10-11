#!/usr/bin/env python3

'''-------------------------------------------------------------
* Pixel Wise Image Analyzer cum Decrypter
* (Recovers data embedded in an image.)
* 07OCT2018
* Authors: Mohammed S. Haque <ubdussamad@gmail.com> , Nishant Ranjan <nishantranjan1998@gmail.com>
* Primarily Built around Python3.x

* This program is intended to work with many methods of
* storing data using image manipulation and is not just supposed
* to recover strings from an image but any kind of binary file
* may it be another image file or a octet-stream application. 
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
import time

img = Image.open('secret.png') #Reading the Image
arr = np.array(img) #Converting the Image into a 2D array
x,y,z  = np.shape(arr) #Reading the dimensions of the array to determine the storage.
arr = arr.ravel() & 1 #Converting every value in the matrix to 0 if it's even else 1.
lis = arr ^ 1 #Noting every value in the matix.

print("The diamentions of the image are: %dx%dx%d pixels."%(x,y,z))

lis = np.array_split(lis,(len(arr)//8)+1) #Splitting the array into groups of 8 bit binary values.

index = 0
for i in lis:
    if not(any(i)):
        break
    index+=1
lis = lis[:index+1] #Terminating the list at the pointer very all 8 bits are 0
f = ''.join([ chr (int (''.join( map(str , i )) , 2)) for i in lis])#Joining the strings and stuff

print("The text is: %s"%f)
