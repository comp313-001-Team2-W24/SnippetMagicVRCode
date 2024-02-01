# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 16:11:46 2024

@author: 14129
"""

# basic_operations.py
import cv2

def read_display_save_image(image_path):
    # Read the image
    img = cv2.imread(image_path)

    # Display the image
    cv2.imshow('Image', img)
    cv2.waitKey(0)  # Wait for a key press to close
    cv2.destroyAllWindows()

    # Save the image
    cv2.imwrite('output.jpg', img)

if __name__ == "__main__":
    read_display_save_image('C:/Users/14129/Desktop/Software Project 2/MagicAR/static/model1.jpg')
