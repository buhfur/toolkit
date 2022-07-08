#!/usr/bin/env python3 
''' 
Ryan McVicker 
7.8.2022
script to convert picture into ascii art


here is the algorithm to do so : 



1. Convert the input image to grayscale.
2. Split the image into M×N tiles.
3. Correct M (the number of rows) to match the image and font aspect ratio.
4. Compute the average brightness for each image tile and then look up a suitable ASCII character for each.

'''

from PIL import Image

image = Image.open('images/natalie.png') 
#convert image to grayscale 
image.convert('L')

#display the image 
image.show()




     

    

