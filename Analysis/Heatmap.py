# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 16:05:10 2020

@author: SS067504
"""
from PIL import Image
import cv2
'''
img = cv2.imread('2.jpeg')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
heatmap_img = cv2.applyColorMap(gray_img, cv2.COLORMAP_BONE)

fin = cv2.addWeighted(heatmap_img, 0.7, img, 0.3, 0)

img = Image.fromarray(fin)
img.save('test.png')
img.show()#heatmap_img.save("heatmap_img.jpg") 
#fin.show()
#fin.save("fin.jpg") 


import matplotlib.pyplot as plt
import numpy as np
import cv2

image = cv2.imread('2.jpeg', 0)
colormap = plt.get_cmap('inferno')
heatmap = (colormap(image) * 2**16).astype(np.uint16)[:,:,:3]
heatmap = cv2.cvtColor(heatmap, cv2.COLOR_RGB2BGR)

cv2.imshow('image', image)
cv2.imshow('heatmap', heatmap)
cv2.waitKey()
'''
import cv2
import numpy as np
import matplotlib.pyplot as plt

frame = cv2.imread("2.jpeg")
lower_black = np.array([0,0,0], dtype = "uint16")
upper_black = np.array([70,70,70], dtype = "uint16")
black_mask = cv2.inRange(frame, lower_black, upper_black)
cv2.imwrite('img.jpg',black_mask)
        
from PIL import Image
im1 = Image.open("2.jpeg")
im2 = Image.open("img.jpg")

newimg = Image.blend(im1, im2, alpha=0.5)
newimg.save("blended.jpg")


image = cv2.imread('blended.jpg', 0)
colormap = plt.get_cmap('inferno')
heatmap = (colormap(image) * 2**16).astype(np.uint16)[:,:,:3]
heatmap = cv2.cvtColor(heatmap, cv2.COLOR_RGB2BGR)
cv2.imwrite('heatmap1.png', heatmap)
cv2.waitKey()#heatmap_img.save("heatmap_img.jpg")