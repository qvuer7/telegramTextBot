import telebot	
from INPUT import * 
from AllAboutText.texts.rendering import *
import time


stage = ""
style = 0
textstage = ""
readymessage = [None for i in range(7)]
text_bottle = ""

stylesMarkup = telebot.types.ReplyKeyboardMarkup()
stylesMarkup.row('Стиль текста 1', 'стиль текста 2')
instructionsMarkUp = telebot.types.ReplyKeyboardMarkup()
instructionsMarkUp.row('/start', '/information', '/getstyles')
yesORnoMarkUp = telebot.types.ReplyKeyboardMarkup()
yesORnoMarkUp.row('Да','нет')
allstylesMarkUp = telebot.types.ReplyKeyboardMarkup()
allstylesMarkUp.row('/getstyles')
startEdittingText = telebot.types.ReplyKeyboardMarkup()
startEdittingText.row('/start_edit_text', '/getstyles')
editT1 = telebot.types.ReplyKeyboardMarkup()
editT1.row('editT1')
messageToSend = ""





@BOT.message_handler(commands = ['start'])
def start_message(message):
	global stage, style, textstage, text_bottle, readymessage
	stage = ""
	style = 0
	textstage = ""
	readymessage = [None for i in range(7)]
	text_bottle = ""

	if message.chat.id == -394279568 or message.chat.id == 682847115:
		BOT.send_message(message.chat.id, reply_markup=instructionsMarkUp, text = "/start пишешь вылазит эта менюшка, уясни бля!!")

		stage = "start done"

@BOT.message_handler(commands = ['information'])
def information_message(message):
	if message.chat.id == -394279568 or message.chat.id == 682847115 or message.chat.id ==-324488479:
		BOT.send_message(message.chat.id, reply_markup=instructionsMarkUp, text = "не ну ты охуел еще и инструкцию бля, я ебал")

@BOT.message_handler(commands = ['getstyles'])
def text_markup_keyboard(message):
	global stage
	stage = 'choosing process1'
	if message.chat.id == -394279568 or message.chat.id == 682847115 or message.chat.id ==-324488479:
		BOT.send_message(message.chat.id, reply_markup=stylesMarkup, text = "выберай бля ")


@BOT.message_handler(commands=['start_edit_text'])
def text_editting(message):
	global stage, style, text_bottle, readymessage, textstage
	if  stage == "style confirmed":
		textstage = 1
		text_bottle = text1_rendering(text = message.text)

		BOT.send_message(message.chat.id, text = text_bottle, reply_markup=yesORnoMarkUp)

	if (stage == "style confirmed") and (message.text.lower() == 'да'):
		textstage = 2
		stage = "text1 confirmed"
		readymessage = readymessage + text_bottle
	else:
		BOT.send_message(message.chat.id, text = 'сука дебил старайся блять! пропиши блять команду /editT1')

@BOT.message_handler(commands=['post_message_in_channel'])
def post_message(message):
	BOT.send_message(message.chat.id, text = 'скинь мне сюда сообщение быстро нахуй')


@BOT.message_handler(content_types=['text'])
def text_style(message):
	global stage, style, text_bottle, readymessage, textstage, messageToSend
	if (message.chat.id == -394279568 or message.chat.id == 682847115 or message.chat.id ==-324488479) and stage =='choosing process1':
		if message.text.lower() == 'стиль текста 1':
			BOT.send_message(message.chat.id, text = set_message())
			stage = "choosen process2"
			style = 1
		if message.text.lower() == 'стиль текста 2':
			BOT.send_message(message.chat.id, text = set_message())
			stage = "choosen process2"
			style = 2
		BOT.send_message(message.chat.id, text = 'Братишка уверен шо хош такой текст ммммм??? '
													 '/start если хош посмотреть все стили ну или на клаву тыкни нет', reply_markup=yesORnoMarkUp)
		time.sleep(1)
	if style == 1:
		if ((message.chat.id == -394279568 or message.chat.id == 682847115 or message.chat.id ==-324488479) and stage =='choosen process2') or  stage == "style confirmed" and textstage == "":
			if message.text.lower() == 'да':
				BOT.send_message(message.chat.id, text = 'БРО сейчас сюда прилетит маркап текста не теряй его!!')
				BOT.send_message(message.chat.id,text = set_message())
				stage = "style confirmed"
				BOT.send_message(message.chat.id,
							 text="брат смари сейчас скинешь короче текст для графы ТЕКСТ1, сообщением типо:ТЕКСТ1 линейная игра(текст который будет между кубков только)!")

		if (message.chat.id == -394279568 or message.chat.id == 682847115 or message.chat.id ==-324488479) and stage == 'choosen process2':
			if message.text.lower() == 'нет':
				BOT.send_message(message.chat.id, text = "клац на кнопку! ", reply_markup=allstylesMarkUp)

		if (message.chat.id == -394279568 or message.chat.id == 682847115 or message.chat.id ==-324488479) and stage == "style confirmed":
			if message.text.lower()[:6] == "текст1":
				textstage = "text1 conformation"
				text_bottle = message.text[7:]
				text_bottle = text1_rendering(text = text_bottle)
				BOT.send_message(message.chat.id, text = set_message(text1 = text_bottle))
				BOT.send_message(message.chat.id, text = 'так текст должен выглядить?')


		if (message.chat.id == -394279568 or message.chat.id == 682847115 or message.chat.id ==-324488479) and textstage == "text1 conformation":
			if message.text.lower() == 'да':
				textstage = "text1 confirmed"
				readymessage[0] = text_bottle
				BOT.send_message(message.chat.id,
								 text="брат смари сейчас скинешь цыфру шоб выбрать эмоджи там все написано 1 хокей  , 2 теннис, 3 - баскетбол, 4 - футбол и тд")

			if message.text.lower() == "нет":
				textstage = ""
				BOT.send_message(message.chat.id, text = "старайся бля, нажми на да", reply_markup=yesORnoMarkUp)

		if (message.chat.id == -394279568 or message.chat.id == 682847115 or message.chat.id ==-324488479) and textstage == "text1 confirmed":
			if message.text.lower() == "1":
				textstage = "emoji conformation"
				text_bottle = 1
				BOT.send_message(message.chat.id, text=set_message(text1=readymessage[0], emoji = text_bottle))
				BOT.send_message(message.chat.id, text='так текст должен выглядить?')
			if message.text.lower() == "2":
				textstage = "emoji conformation"
				text_bottle = 2
				BOT.send_message(message.chat.id, text=set_message(text1=readymessage[0], emoji = text_bottle))
				BOT.send_message(message.chat.id, text='так текст должен выглядить?')
			if message.text.lower() == "3":
				textstage = "emoji conformation"
				text_bottle = 3
				BOT.send_message(message.chat.id, text=set_message(text1=readymessage[0], emoji = text_bottle))
				BOT.send_message(message.chat.id, text='так текст должен выглядить?')
			if message.text.lower() == "4":
				textstage = "emoji conformation"
				text_bottle = 4
				BOT.send_message(message.chat.id, text=set_message(text1=readymessage[0], emoji = text_bottle))
				BOT.send_message(message.chat.id, text='так текст должен выглядить?')


		if (message.chat.id == -394279568 or message.chat.id == 682847115 or message.chat.id ==-324488479) and textstage == "emoji conformation":
			if message.text.lower() == 'да':
				textstage = "emoji confirmed"
				readymessage[1] = text_bottle
				BOT.send_message(message.chat.id,
								 text="брат смари сейчас скинешь короче текст для графы ТЕКСТ2, сообщением типо:ТЕКСТ2 ,блаблабла")

			if message.text.lower() == "нет":
				textstage = "text1 confirmed"
				BOT.send_message(message.chat.id, text = "старайся бля, нажми на да", reply_markup=yesORnoMarkUp)






		if (message.chat.id == -394279568 or message.chat.id == 682847115 or message.chat.id ==-324488479) and textstage == "emoji confirmed":
			if message.text.lower()[:6] == "текст2":
				textstage = "text2 conformation"
				text_bottle = message.text[7:]
				text_bottle = text2_rendering(text = text_bottle)
				BOT.send_message(message.chat.id, text = set_message(text1 = readymessage[0], text2 = text_bottle))
				BOT.send_message(message.chat.id, text = 'так текст должен выглядить?')


		if (message.chat.id == -394279568 or message.chat.id == 682847115 or message.chat.id ==-324488479) and textstage == "text2 conformation":
			if message.text.lower() == 'да':

				readymessage[2] = text_bottle
				BOT.send_message(message.chat.id,
								 text="брат смари сейчас скинешь короче текст для графы ТЕКСТ3, сообщением типо:ТЕКСТ3 ,блаблабла")
				textstage = "text2 confirmed"
			if message.text.lower() == "нет":

				textstage ="emoji conformation"
				BOT.send_message(message.chat.id, text = "старайся бля, нажми на да", reply_markup=yesORnoMarkUp)



		if (message.chat.id == -394279568 or message.chat.id == 682847115 or message.chat.id ==-324488479) and textstage == "text2 confirmed":
			if message.text.lower()[:6] == "текст3":
				textstage = "text3 conformation"
				text_bottle = message.text[7:]
				text_bottle = text3_rendering(text = text_bottle)



				BOT.send_message(message.chat.id, text = set_message(text1 = readymessage[0], text2 = readymessage[2], text3 = text_bottle))
				BOT.send_message(message.chat.id, text = 'так текст должен выглядить?')


		if (message.chat.id == -394279568 or message.chat.id == 682847115 or message.chat.id ==-324488479) and textstage == "text3 conformation":
			if message.text.lower() == 'да':

				readymessage[3] =text_bottle
				BOT.send_message(message.chat.id,
								 text="брат смари сейчас скинешь короче текст для графы ТЕКСТ4, сообщением типо:ТЕКСТ4 ,блаблабла")
				textstage = "text3 confirmed"
			if message.text.lower() == "нет":

				textstage ="text2 conformation"
				BOT.send_message(message.chat.id, text = "старайся бля, нажми на да", reply_markup=yesORnoMarkUp)




		if (message.chat.id == -394279568 or message.chat.id == 682847115 or message.chat.id ==-324488479) and textstage == "text3 confirmed":
			if message.text.lower()[:6] == "текст4":
				textstage = "text4 conformation"
				text_bottle = message.text[7:]
				text_bottle = text2_rendering(text = text_bottle)
				BOT.send_message(message.chat.id, text = set_message(text1 = readymessage[0],emoji=readymessage[1],  text2 = readymessage[2], text3 = readymessage[3] , text4= text_bottle))
				BOT.send_message(message.chat.id, text = 'так текст должен выглядить?')


		if (message.chat.id == -394279568 or message.chat.id == 682847115 or message.chat.id ==-324488479) and textstage == "text4 conformation":
			if message.text.lower() == 'да':

				readymessage[4] = text_bottle

				BOT.send_message(message.chat.id,
								 text="брат смари сейчас скинешь короче текст для графы ТЕКСТ5, сообщением типо:ТЕКСТ5 ,блаблабла")
				textstage = "text4 confirmed"
			if message.text.lower() == "нет":

				textstage ="text3 conformation"
				BOT.send_message(message.chat.id, text = "старайся бля, нажми на да", reply_markup=yesORnoMarkUp)






		if (message.chat.id == -394279568 or message.chat.id == 682847115 or message.chat.id ==-324488479) and textstage == "text4 confirmed":
			if message.text.lower()[:6] == "текст5":
				textstage = "text5 conformation"
				text_bottle = message.text[7:]
				text_bottle = text3_rendering(text = text_bottle)



				BOT.send_message(message.chat.id, text = set_message(text1 = readymessage[0],emoji=readymessage[1],  text2 = readymessage[2], text3 = readymessage[3] , text4= readymessage[4], text5 = text_bottle))
				BOT.send_message(message.chat.id, text = 'так текст должен выглядить?')


		if (message.chat.id == -394279568 or message.chat.id == 682847115 or message.chat.id ==-324488479) and textstage == "text5 conformation":

			if message.text.lower() == 'да':

				readymessage[5] = text_bottle
				BOT.send_message(message.chat.id,
								 text="брат смари сейчас скинешь короче текст для графы ТЕКСТ6, сообщением типо:ТЕКСТ6 ,блаблабла")
				textstage = "text5 confirmed"
			if message.text.lower() == "нет":

				textstage ="text4 conformation"
				BOT.send_message(message.chat.id, text = "старайся бля, нажми на да", reply_markup=yesORnoMarkUp)








		if (message.chat.id == -394279568 or message.chat.id == 682847115 or message.chat.id ==-324488479) and textstage == "text5 confirmed":
			if message.text.lower()[:6] == "текст6":
				textstage = "text6 conformation"
				text_bottle = message.text[7:]
				text_bottle = text3_rendering(text = text_bottle)



				BOT.send_message(message.chat.id, text = set_message(text1 = readymessage[0],emoji=readymessage[1],  text2 = readymessage[2], text3 = readymessage[3] , text4= readymessage[4], text5 = readymessage[5], text6 = text_bottle))
				BOT.send_message(message.chat.id, text = 'так текст должен выглядить?')


		if (message.chat.id == -394279568 or message.chat.id == 682847115 or message.chat.id ==-324488479) and textstage == "text6 conformation":
			if message.text.lower() == 'да':

				readymessage[6] = text_bottle
				BOT.send_message(message.chat.id,
								 text="брат смари сейчас скинешь короче текст для графы ТЕКСТ7, сообщением типо:ТЕКСТ7 ,блаблабла")
				textstage = "text6 confirmed"
			if message.text.lower() == "нет":

				textstage ="text5 conformation"
				BOT.send_message(message.chat.id, text = "старайся бля, нажми на да", reply_markup=yesORnoMarkUp)



		if (message.chat.id == -394279568 or message.chat.id == 682847115 or message.chat.id ==-324488479) and textstage == "text6 confirmed":
			if message.text.lower()[:6] == "текст7":
				textstage = "text7 conformation"
				text_bottle = message.text[7:]
				text_bottle = text3_rendering(text = text_bottle)



				BOT.send_message(message.chat.id, text = set_message(text1 = readymessage[0],emoji=readymessage[1],  text2 = readymessage[2], text3 = readymessage[3] , text4= readymessage[4], text5 = readymessage[5], text6 = readymessage[6], text7 = text_bottle))
				BOT.send_message(message.chat.id, text = 'так текст должен выглядить?')


		if (message.chat.id == -394279568 or message.chat.id == 682847115 or message.chat.id ==-324488479) and textstage == "text7 conformation":
			if message.text.lower() == 'да':

				readymessage[7] = text_bottle
				print(readymessage)
				messageToSend = set_message(text1 = readymessage[0],emoji=readymessage[1],  text2 = readymessage[2], text3 = readymessage[3] , text4= readymessage[4], text5 = readymessage[5], text6 = readymessage[6], text7 = readymessage[7])
				BOT.send_message(message.chat.id, text =messageToSend)
				textstage = "text7 confirmed"

			if message.text.lower() == "нет":

				textstage ="text6 conformation"
				BOT.send_message(message.chat.id, text = "старайся бля, нажми на да", reply_markup=yesORnoMarkUp)


BOT.polling()