import telebot

import telebot

with open('token.txt', 'r') as file:
    token = file.read()

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    username = message.chat.username
    print("username=%s"%username)
    bot.send_message(message.chat.id, 'Привет, %s, ты написал мне /start'%username)

bot.polling()

choice = input('Press Q to Quit')
if choice == 'q':
    import sys
    sys.exit(0)