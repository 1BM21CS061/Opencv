import numpy as np
import matplotlib.pyplot as plt 
import cv2 

def display(img,name):
    while True:
        cv2.imshow(name,img)

        if cv2.waitKey(0) == ord('q'):
            cv2.destroyAllWindows()
            return

img = cv2.imread("./rainbow-sq.jpg",0)
plt.imshow(img,cmap='gray')
plt.show()

ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
plt.imshow(thresh1,cmap='gray')
plt.show()