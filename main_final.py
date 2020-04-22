
#-----------------------------import lib---------------------------------------
import telepot
import time
import cv2
import numpy as np
from time import sleep

import urllib.request as urllib
import re


#------------------------------------------------------------------------------

#---------------------------Camera Image Take---------------------------------
def capture_img():
    camera_port = 0
    ramp_frames = 30
    camera = cv2.VideoCapture(camera_port)

    def get_image():
        retval, im = camera.read()
        return im

    print("Taking image...")
    camera_capture = get_image()

    file = "image_default.jpeg"
    cv2.imwrite(file, camera_capture)
#------------------------------------------------------------------------------

#--------------------------Canny Edge Algorithm--------------------------------
def auto_canny(image, sigma=0.33):
    # compute the median of the single channel pixel intensities
    v = np.median(image)
    # apply automatic Canny edge detection using the computed median
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))
    edged = cv2.Canny(image, lower, upper)

    # return the edged image
    return edged
#------------------------------------------------------------------------------


#-------------------------Count fuction for pixel calculation------------------
def cal_count(edges,x1,y1,x2,y2):
    #global edges
    count=0

    for y in range(y1,y2):
        for x in range(x1,x2):
            if edges[y][x] != 0:
                #print "[",x,"]","[",y,"] =",edges[x][y]
                count+=1
    return count
#------------------------------------------------------------------------------

def solt_info():
    img = cv2.imread('image_default.jpeg',0)     #import img
    edges=auto_canny(img)               #send for canny edges calculation
    #height = np.size(img, 0)
    #width = np.size(img, 1)

    #cv2.rectangle(edges, (98, 117),( 214, 191), (255,0,0), 2)
    slot_1=cal_count(edges, 98, 117, 214, 191)

    #cv2.rectangle(edges, (71, 257), (204, 360), (255,0,0), 2)
    slot_2=cal_count(edges, 71, 257, 204, 360)

    #cv2.rectangle(edges_org, (381, 105),( 538, 190), (255,0,0), 2)
    slot_3=cal_count(edges, 381, 105, 538, 190)

    #cv2.rectangle(edges_org, (383, 247),( 553, 346), (255,0,0), 2)
    slot_4=cal_count(edges, 383, 247, 553, 346)
    #rec4=cv2.rectangle(edges_org, (383, 247),( 553, 346), (255,0,0), 2)
    #cv2.imshow('rectangle4',rec4)

    slots = [slot_1,slot_2,slot_3,slot_4]
    
            

    for s in slots:
        if s > 50:
            slots[slots.index(s)] = "Not Available"
        else:
            slots[slots.index(s)] = "Available"
    
   
    return slots


#-----------------------send_slot info------------------------------------------
def send_txt(chat_id, msg):
    bot.sendMessage(chat_id, msg)

#-----------------------send_slot_photo----------------------------------------
def send_photo(chat_id, photo, caption=None):
    msg1 = bot.sendPhoto(chat_id=chat_id, photo=open(photo, "rb"))
    
    #file_id = msg.photo[0].file_id
     
    #bot.sendPhoto(photo=file_id)


    """
    with open(photo, mode='r') as f:   
        bot.sendPhoto(chat_id,f, caption)
    
    cv2.imshow('image',img)
    k=cv2.waitKey(0)
    if k==27:
        cv2.destroyAllWindows()
    elif k==ord('s'):
        cv2.imwrite('image.jpeg',img)
        cv2.destroyAllWindows()
    
    with open(photo, mode='r') as f:  #mode='r'
        cv2.imshow('image',f)
        #bot.sendPhoto(chat_id,f, caption)
"""
#-------------------------input masg handle loop -------------------------------
def handle(msg):
    print( msg)
    try:
        print("Enter")
        #date = msg['date']
        #usr_name = msg['from']['username']
        chat_id = msg['chat']['id']
        #msg_id = msg['message_id']
        command = msg['text']
        print(chat_id)
        print(command)
    except:
        print("Unexpected msg")
        pass
    else:
        print('Got command: ', command)

        if command == "photo":
            #send_photo(chat_id, "t.png")
            try:
                capture_img()
            except:
                print ("fail to capture Image")
            else:
                send_photo(chat_id, "image_default.jpeg")

        if command == "slots":
            try:
                f1=0
                f2=0
                f3=0
                f4=0
                capture_img()
                time.sleep(1)
                slots = solt_info()
                #print(slots[0])
                if(slots[0]=="Not Available"):
                    f1=1
            
                if(slots[1]=="Not Available"):
                    f2=1
                   
                if(slots[2]=="Not Available"):
                    f3=1
                    
                if(slots[3]=="Not Available"):
                    f4=1

                #datafromwebsite4=urllib.urlopen("https://api.thingspeak.com/update?api_key=70HJS9ECYJCTT7X2&f"+'&field1=%s&field2=%s&field3=%s&field4=%s' % (f1, f2,f3,f4));
                    

                
                
            except:
                print("Fail to send slots info")
            else:
                msg = "Parking Slots : \n" +"Slot-1: "+slots[0]+" Rs 50/hr"+"\n" + "Slot-2: "+slots[1]+" Rs 70/hr"+"\n"+ "Slot-3: "+slots[2]+" Rs 30/hr"+"\n"+ "Slot-4: "+slots[3]+" Rs 50/hr"
                send_txt(chat_id, msg)
        
            

        if command == "available slots":
            try:
                capture_img()
                time.sleep(1)
                slots = solt_info()
            except:
                print("Fail to send slots info")
            else:
                msg = "Available Slots \n"
                count=0
                for s_no, s in enumerate(slots, start=1):
                    
                    if s == "Available":
                        msg +="slot: "+ str(s_no) +"\n"
                        count+=1
                        
                if count == 0:
                    msg = "Parking Full"

                send_txt(chat_id, msg)
                        #commands(chat_id, msg_id, date, command, usr_name, first_name, last_name)









#-------------------------Digi-server-bot config -------------------------------
#bot = telepot.Bot('768091658:AAFnWx_BPy2sLmc6W8YhLSkhtBmt_zNpgHk')
#bot = telepot.Bot('1069006266:AAGTIZy5tNG4LV21JlpqwnrgHO_cMQagtSw')
bot = telepot.Bot('825556491:AAH_6SYVb631L3fSOz7315PucQW266s2lb0')

bot.message_loop(handle)
print ('I am listening...')

while 1:
    time.sleep(1)
