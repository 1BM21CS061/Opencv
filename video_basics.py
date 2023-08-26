import cv2

#cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture("../Videos/cars_test.mp4")

def main():
    if cap.isOpened() == False:
        print("ERROR IN PLAYING VIDEO")
        return
    
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    while cap.isOpened():
        ret,frame = cap.read()      #(flag variable, frame object)
        #gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

        if ret==True:
            cv2.imshow('frame',frame)
            #cv2.imshow('gray',gray)

            if cv2.waitKey(1) & 0xFF==ord('q'):     #& -> bitwise and operator
                print(width,height)
                break
        else:
            cap.release()
 
    
    cv2.destroyAllWindows()

main()    
