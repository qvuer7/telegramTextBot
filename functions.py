import telebot
from  INPUT import *


@BOT.message_handler(commands = ['start'])
def send_text(bot, chat_id, file): 
	f = open(file).read()
	if f[14] == "1":
		bot.send_message(chat_id, f[15:])




		