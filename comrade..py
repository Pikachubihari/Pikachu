import logging
from db import *
from telethon.sessions import StringSession
from telethon import TelegramClient, events
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from telethon.tl.functions.channels import GetFullChannelRequest, JoinChannelRequest, InviteToChannelRequest
import time

logging.basicConfig(level=logging.INFO)
OWNER_IDS = [2140114063, 5388066357, 2067682959] # edit your id
client = TelegramClient(pp
    StringSession("Your string session here"),
    api_id=Your api id,
    api_hash="Your api hash"
).start()
# import the time module





#-------------Control Panel----------------#
photo = 'Your Telegraph Link'
TIME_INTERVAL = 1 #An Integer Always add time in minutes
OPTION = 2 #1 for send media + Caption and 2 for only message

#-------------------------------------------#

def countdown(t):
	
	while t:
		mins, secs = divmod(t, 60)
		timer = '{:02d}:{:02d}'.format(mins, secs)
		print(timer, end="\r")
		time.sleep(1)
		t -= 1
	
	print('Comrade always OP!!')


t = TIME_INTERVAL*1



  
