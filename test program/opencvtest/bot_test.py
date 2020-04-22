from io import BytesIO
import telepot
import cv2
import time
bot = telepot.Bot('768091658:AAFnWx_BPy2sLmc6W8YhLSkhtBmt_zNpgHk')
def handle(msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        print(content_type, chat_type, chat_id)
        if content_type == 'text':
            bot.sendMessage(chat_id, "You said '{}'".format(msg["text"]))
           
            
            bot.sendPhoto(chat_id, 'image.jpeg')

            #cv2.destroyAllWindows()
            
            #caption = NULL, disable_notification = FALSE,
             #  reply_to_message_id = NULL, reply_markup = NULL, parse_mode = NULL)
                
            
bot.message_loop(handle)
print ('Listening ...')
while 1:
    time.sleep(10)
        
