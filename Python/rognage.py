# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 15:08:29 2021

@author: Hp
"""

import numpy as np
import matplotlib.pyplot as plt
from os.path import join
import skimage.io as skio

plt.close('all')

filename = r'final7.jpg'
dirpath = r'..\Images_test'
filepath = join(dirpath, filename)

img = skio.imread(filepath)

plt.figure(1)
plt.imshow(img), plt.title('Original image')

def rognage(image):
    
    dtype=image.dtype
    
    new_img=np.zeros((1800,1650,3), dtype)
    
    for i in range(0,1800):
        for j in range(0,1650):
            new_img[i,j]=image[i+600,j+650]
    
    return new_img


img_rognee = rognage(img)

plt.figure(2)
plt.imshow(img_rognee), plt.title('Image rognée')