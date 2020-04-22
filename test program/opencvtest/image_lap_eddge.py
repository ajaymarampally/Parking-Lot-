import cv2
import numpy as np
cap = cv2.VideoCapture(0); #0 for external cam 1 for laptop cam


while(cap.isOpened()):
    ret,frame = cap.read()
    if ret == True:
        
        laplacian = cv2.Laplacian(frame,cv2.CV_64F)
        #sobelx = cv2.Sobel(frame,cv2.CV_64F,1,0,ksize=5)
        #sobely = cv2.Sobel(frame,cv2.CV_64F,0,1,ksize=5)
        
        
        #cv2.imshow('sobelx',sobelx)
        #cv2.imshow('sobely',sobely)
        cv2.imshow('originalframe',frame)
        cv2.imshow('Laplacian',laplacian)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break


cap.release()
cv2.destroyAllWindows()
 
