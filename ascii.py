
import os
import time
from PIL import Image
import numpy as np
import sys
import cv2

def initA():
    
    # captures the webcam
    vidcap = cv2.VideoCapture(1)
    success,image = vidcap.read()
    count = 0
    while success:
        cv2.imwrite("./images/frame%d.jpg" % count, image)     # save frame as JPEG file      
        success,image = vidcap.read()
        count += 1


    # pass the image as command line argument
        image_path = './images/frame' + str(count - 1) + '.jpg'
        img = Image.open(image_path)

        # resize the image
        width, height = img.size
        aspect_ratio = height/width
        new_width = 125
        new_height = aspect_ratio * new_width * 0.55
        img = img.resize((new_width, int(new_height)))
        # new size of image
        # print(img.size)

        # convert image to greyscale format
        img = img.convert('L')

        pixels = img.getdata()

        # replace each pixel with a character from the ascii character list
        chars = ["B","S","#","&","@","$","%","*","!",":","."]
        new_pixels = [chars[pixel//25] for pixel in pixels]
        new_pixels = ''.join(new_pixels)

        # split string of chars into multiple strings of length equal to new width and create a list

        new_pixels_count = len(new_pixels)
        ascii_image = [new_pixels[index:index + new_width] for index in range(0, new_pixels_count, new_width)]
        ascii_image = "\n".join(ascii_image)
        print(ascii_image)

        # delete the image afterward to save storage space

        os.remove('./images/frame' + str(count - 1) + '.jpg')