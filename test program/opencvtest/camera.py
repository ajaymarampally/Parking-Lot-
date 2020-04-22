import cv2

camera = cv2.VideoCapture(0)

ret,im = camera.read()

cv2.imwrite('test.png',im)

img =cv2.imread('test.png',1)
print(img)
cv2.imshow('image',img)

