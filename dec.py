from PIL import Image
import numpy as np
import time

img = Image.open('secret.png') #Reading the Image
arr = np.array(img) #Converting the Image into a 2D array
x,y,z  = np.shape(arr) #Reading the dimensions of the array to determine the storage.
arr = arr.ravel() & 1 #Converting every value in the matrix to 0 if it's even else 1.
lis = arr ^ 1 #Noting every value in the matix.

index = 19955
import math
print("The diamentions of the image are: %dx%dx%d pixels."%(x,y,z))
jj = lis[:index+1]
ll = len(jj)
lis = np.array_split( jj , math.ceil(ll/8) ) #Splitting the array into groups of 8 bit binary values.
print(1)


lis = lis#Terminating the list at the pointer very all 8 bits are 0
print(2)
print(lis[0])

tmp = []
for i in lis:
    out = 0
    for bit in i:
        out = (out << 1) | bit
    tmp.append(out)
print(3)
lis = tmp
bytes_array = bytearray( lis )
print(max(lis))
f = open('new_p.jpg','wb')
f.write(bytes_array)
f.close()
