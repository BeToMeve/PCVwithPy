#coding: utf-8
'''
Created on 2015年7月23日

@author: Administrator
'''
from PIL import Image
from numpy import *
import imtools
from pylab import *
from matplotlib.pyplot import show, imshow, figure
im = array(Image.open('sunset.jpg').convert('L'))
im2,cdf = imtools.histeq(im)
im2=255.0*(im2/255.0)**2
gray()
imshow(im2)
figure()
hist(im.flatten(),128)
show()