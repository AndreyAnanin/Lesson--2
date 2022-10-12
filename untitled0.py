import telebot
import telebot.types

TOKEN ="5638130954:AAESPDRRuj5T1oiTUBVntmjIyjJEmHe7pA8"

bot = telebot.TeleBot(TOKEN)

# # словарик, есть ключ который что то выдает если его написать
# #свойство( можно на один метод создать много свойств)
# #Свойство для обработки(по умолчанию)
# #Если подходит едет дальше
# @bot.message_handler(commands=['start', 'help'])
# #принимает сообщение на которое реагировало(пропихнет вниз)
# def send_welcome(message):
#  	#бот ответь(варианты ответа)
#     bot.reply_to(message, "Howdy, how are you doing?")

# @bot.message_handler(commands=['hi'])

# def send_name(message):
#     bot.reply_to(message, "Hi" + message.)
# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
#   	 bot.reply_to(message, message.text)

# echo - слушать(что написали, то и ответили)
@bot.message_handler(commands=['hi'])
def Hi_name(message):
    name = message.from_user.first_name
    twoname = message.from_user.id
    response = f'Привет, {name} , { twoname}!'
    bot.send_message(message.chat.id, response)

bot.infinity_polling()


























