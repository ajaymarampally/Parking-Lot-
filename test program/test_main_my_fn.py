import telepot
import time
import cv2
import numpy as np

def handle(msg):
    print(msg)
    """try:
        date = msg['date']
        usr_name = msg['from']['username']
        chat_id = msg['chat']['id']
        msg_id = msg['message_id']
        command = msg['text']
    except:
        print("Unexpected msg")
        pass
    else:
        print('Got command: ', command)
"""
bot = telepot.Bot('768091658:AAFnWx_BPy2sLmc6W8YhLSkhtBmt_zNpgHk')
bot.message_loop(handle)
print ('I am listening...')

while 1:
    time.sleep(1)
