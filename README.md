# Steganography
Simple steganography tool for embedding data into image matrices.

## Description
This tools embeds any piece of data may it be a audio,video or a binary executable
into an image without any significant change in the image itself. (Apart from the image becoming a little brighter)

## Dependencies
1. Numpy can be installed by `pip install numpy`
2. Pillow can be installed by `pip install pillow` 

## Usage
A quick run of this python script should do the job provided the paths (relative or real) to the target image to modify
and the data which is to be embedded.


##### Embedding the data into image :-
```
$ chmod +x enc.py
$ ./enc.py [path_to_carrier_image] [path_to_data]

// Example: ./enc.py [image.jpg] [audio.aiff]
// Where: image.jpg is the image which will carry the data , 
// and the data would be the audio.aiff file.
```
>Note: Running this on an image will not modify the image with data itself but will create a new image named 
*secret.png* which will then be read by the decrypter so the data could be extracted from it.

##### Extracting data from the image :-
```
$ chmod +x dec.py
$ ./dec.py
```
>Note: You are supposed to run this script in the same folder where you have the **output** *secret.png* from the
encrypter program and running this script will produce an extension less file named *recovred_data*.
