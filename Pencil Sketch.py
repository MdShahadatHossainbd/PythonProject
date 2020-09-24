#Description: This program converts an image to a pencil sketch

#pip install opencv-python

#import the library
import cv2

#Get the image location and the image file name
img_location = '/home/sh/Downloads/'
filename = 'shahadathossain.jpg'

#Read in the image
img = cv2.imread(img_location+filename)

#convert the image to gray scale
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Invert the image
inverted_gray_image = 255 - gray_image

#Blur the image by gaussian function
blurred_img = cv2.GaussianBlur(inverted_gray_image,(21,21),0)

#Invert the blurred image
inverted_blurred_image = 255 - blurred_img

#Create the pencil sketch image
pencil_sketch_IMG = cv2.divide(gray_image,inverted_blurred_image, scale=256.0)

#show the image
cv2.imshow('Original Image', img)
cv2.imshow('New Image', pencil_sketch_IMG)
cv2.waitKey(0)
