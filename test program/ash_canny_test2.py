import cv2
import numpy as np
def auto_canny(image, sigma=0.33):
    # compute the median of the single channel pixel intensities
    v = np.median(image)
    # apply automatic Canny edge detection using the computed median
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))
    print(lower)
    print(upper)
    edged = cv2.Canny(image, lower, upper)

    # return the edged image
    return edged


def cal_count(edges,x1,y1,x2,y2):
    #global edges
    count=0

    for y in range(y1,y2):
        for x in range(x1,x2):
            if edges[y][x] != 0:
                #print ("[",x,"]","[",y,"] =",edges[y][x])
                count+=1
    return count


img = cv2.imread('image_default.jpeg',0)     #import img
edges=auto_canny(img)
#cv2.imshow('frame',edges)

slot_1=cal_count(edges, 98, 117, 214, 191)
imgrec1=cv2.rectangle(edges, (98, 117),( 214, 191), (255,0,0), 2)
print(slot_1)
cv2.imshow('rec1',imgrec1)


slot_2=cal_count(edges, 71, 257, 204, 360)
imgrec2=cv2.rectangle(edges, (71, 257), (204, 360), (255,0,0), 2)
cv2.imshow('rec2',imgrec2)


slot_3=cal_count(edges, 381, 105, 538, 190)
imgrec3=cv2.rectangle(edges, (381, 105),( 538, 190), (255,0,0), 2)
cv2.imshow('rec3',imgrec3)


slot_4=cal_count(edges, 410, 255, 557, 332)
imgrec4=cv2.rectangle(edges, (410, 255),( 557, 332), (255,0,0), 2)
cv2.imshow('rec4',imgrec4)

slots = [slot_1,slot_2,slot_3,slot_4]

for s in slots:
    print(s)
    if s > 50:
        print('found occupied')
            #slots[slots.index(s)] = "Not Available"
    else:
        print('found avaiable')
            #slots[slots.index(s)] = "Available"

