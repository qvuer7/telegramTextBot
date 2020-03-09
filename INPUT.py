import telebot


API_TOKEN = open("API.txt").read()
BOT = telebot.TeleBot(API_TOKEN)
CHAT_ID= "-394279568"
TEXT_FILE = "message.txt"

class stage_controller:
    def __init__(self):
        self.stage = 0

