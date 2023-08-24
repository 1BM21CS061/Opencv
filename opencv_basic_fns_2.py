import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("KOA_Nassau_2697x1517.jpg")
'''while True:
    cv2.imshow("Image",img)

    cv2.waitKey()

    if cv2.waitKey(1000)==ord('q'): 
        print(ord('q'))                 #waits for a user to enter a key in the specified time frame
        break                           #returns the hexcode value of the pressed key'''

img = np.zeros(shape=(900,900,3),dtype=np.int16)

cv2.rectangle(img,pt1=(0,0),pt2=(120,400),color=(0,255,0))
#pt1 = top left point pt2 = bottom right point 

cv2.circle(img=img, center = (50,50), radius = 130,color = (0,0,255))
#filled in shapes => thickness = -1

cv2.putText(img,text="Hello",org=(10,500),thickness=5,fontScale = 4,fontFace = cv2.FONT_HERSHEY_COMPLEX,color=(255,255,255))

plt.imshow(img)
plt.show()

