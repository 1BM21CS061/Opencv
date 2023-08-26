import cv2
import matplotlib.pyplot as plt

def display(img,name):
    while True:
        cv2.imshow(name,img)

        if cv2.waitKey(0) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

img = cv2.imread("./KOA_Nassau_2697x1517.jpg")
display(img,"original")
img[:,:,0:2] = 0
display(img,"isolated")
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
display(img_gray,"grayed")

mask_inv = cv2.bitwise_not(img_gray)
display(mask_inv,"mask")

bk = cv2.bitwise_or(img,img,mask= mask_inv)
display(bk,"answer")
