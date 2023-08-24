import numpy as np
import matplotlib.pyplot as plt 
import cv2
from PIL import Image

img = cv2.imread('KOA_Nassau_2697x1517.jpg')
#print(type(img))
#plt.imshow('KOA_Nassau_2697x1517.jpg')
#plt.show()

#MATPLOTLIB -> RGB
#OPENCV -> BGR 

img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.imshow(img)
#plt.show()

new_img= cv2.resize(img,(400,600))   #resizing images according to your dimensions
print(new_img.shape)
plt.imshow(new_img)
#plt.show()

w_ratio = h_ratio = 0.5
new_img = cv2.resize(img,(0,0),img,w_ratio,h_ratio)   #resizing images according to ratios

cv2.imwrite("NEW_IMG.jpg",new_img)