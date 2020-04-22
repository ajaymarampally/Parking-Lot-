import cv2

cap = cv2.VideoCapture(0); #0 for external cam 1 for laptop cam


ret,img = cap.read()

cv2.imshow('image',img)
k=cv2.waitKey(0)


if k==27:
    cv2.destroyAllWindows()
elif k==ord('s'):
    cv2.imwrite('image_default.jpeg',img)
    cv2.destroyAllWindows()
cap.release()
