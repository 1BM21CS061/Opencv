import cv2
import matplotlib.pyplot as plt
import numpy as np

def display(img,name):
    while True:
        cv2.imshow(name,img)

        if cv2.waitKey(0) == ord('q'):
            cv2.destroyAllWindows()
            break

img = cv2.imread("./41g7KY1DWgL._AC_UF1000,1000_QL80_.jpg")

display(img,"original")

img_gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
display(img_gray,"grayed")

mask_img = cv2.bitwise_not(img_gray)
display(mask_img,"mask")

'''white_background = np.full(img.shape,255,dtype=np.uint8)
bk = cv2.bitwise_or(white_background,white_background,mask = mask_img)
display(bk,"mask_c")
'''

display(cv2.bitwise_and(img,img,mask=mask_img),"result")

#print(bk.shape)
