# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 15:08:29 2021

@author: Hp
"""

import numpy as np
import matplotlib.pyplot as plt
from os.path import join
import skimage.io as skio
from picamera import PiCamera
from time import sleep

def photo_rognage(filename = r'final.jpg'):
    
    dirpath = r'..\Images_test'
    filepath = join(dirpath, filename)
    
    camera = PiCamera()
    camera.start_preview()
    sleep(3) #Au moins 2 secondes pour que la caméra prenne une bonne photo
    camera.capture(filepath)
    camera.stop_preview()

    img = skio.imread(filepath)    
    dtype=img.dtype
    
    new_img=np.zeros((1800,1650,3), dtype)
    
    for i in range(0,1800):
        for j in range(0,1650):
            new_img[i,j]=img[i+600,j+650]
    
    return new_img


img_rognee = photo_rognage('Image')

plt.figure(1)
plt.imshow(img_rognee), plt.title('Image rognée')