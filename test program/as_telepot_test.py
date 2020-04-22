# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 23:00:37 2019

@author: Ashish
"""

"""import telepot
 bot = telepot.Bot('768091658:AAFnWx_BPy2sLmc6W8YhLSkhtBmt_zNpgHk')
 bot.getMe()
{'first_name': 'Your Bot', 'username': 'YourBot', 'id': 123456789}
###############
import telepot
from pprint import pprint
response = bot.getUpdates()
pprint(response)
[{'message': {'chat': {'first_name': 'Nick',
                       'id': 999999999,
                       'type': 'private'},
              'date': 1465283242,
              'from': {'first_name': 'Nick', 'id': 999999999},
              'message_id': 10772,
              'text': 'Hello'},
  'update_id': 100000000}]"""
from pprint import pprint
import telepot
from telepot.loop import MessageLoop
def handle(msg):
    pprint(msg)

MessageLoop(bot, handle).run_as_thread()