from varData import adminToken

import telebot
import time

TOKEN = "1815441409:AAE22OLP3DOblzIWWk2IvjN0Q_TcniS2YSo"
bot = telebot.TeleBot(TOKEN)

def getargs(text):
  -args = text.split()[1:]
  return _args

@bot.message_handler(commands=["start"])
def start(message):
  bot.send_message(message.chat.id,"ciao")
  
  while True:
  try:
    bot.polling()
  except:
    time.sleep(5)
