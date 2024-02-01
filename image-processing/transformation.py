# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 16:12:50 2024

@author: 14129
"""

# transformations.py
import cv2

def resize_image(image_path, width, height):
    # Read the image
    img = cv2.imread(image_path)

    # Resize the image
    resized_img = cv2.resize(img, (width, height))

    # Display the resized image
    cv2.imshow('Resized Image', resized_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def crop_image(image_path, start_x, start_y, width, height):
    # Read the image
    img = cv2.imread(image_path)

    # Crop the image
    cropped_img = img[start_y:start_y+height, start_x:start_x+width]

    # Display the cropped image
    cv2.imshow('Cropped Image', cropped_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    resize_image('static/model1.jpg', 200, 200)
    crop_image('static/model1.jpg', 50, 50, 100, 100)
