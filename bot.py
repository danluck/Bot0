import telebot

with open('token.txt', 'r') as file:
    token = file.read()

bot = telebot.TeleBot(token)

messageCounter = 1

def printUserInfo(message):
    global messageCounter
    username = message.chat.username
    print("counter=%d, username=%s"%(messageCounter,username))
    messageCounter += 1

def sendStartMessage(message):
    printUserInfo(message)
    bot.send_message(message.chat.id, \
        'Привет, %s, ты написал мне /start'%message.chat.username)

@bot.message_handler(commands=['start'])
def start_message(message):
    sendStartMessage(message)

@bot.message_handler(content_types=['text'])
def send_text(message):
    messageText = message.text.lower()
    printUserInfo(message)
    if messageText == 'привет':
        bot.send_message(message.chat.id, 'Привет, мой создатель')
    elif messageText == 'пока':
        bot.send_message(message.chat.id, 'Прощай, создатель')
    else:
        bot.send_message(message.chat.id, 'echo=%s'%message.text)

bot.polling()