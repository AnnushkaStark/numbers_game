import telebot 
import random
bot = telebot.TeleBot('6029515865:AAGYMP9S2QjY3e69ekjkHClJnOmziEhMiTY')
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,'Привет, поиграем в угадай число')
    bot.send_message(message.chat.id,'Я загадаю число от 1 до 100 попробуй его угадать')
    bot.send_message(message.chat.id,'Введите число от 1 до 100')


bot_num  = random.randint(1,100)    
@bot.message_handler(func= lambda message:True)
def get_text_message(message):
    user_message = message.text.lower()
    if  user_message.isalpha():
        bot.send_message(message.chat.id,'А может все таки число от 1 го до 100')
    if user_message.isdigit() and 1 > int(user_message) > 100:
        bot.send_message(message.chat.id,'А может все таки число от 1 го до 100')
    if user_message.isdigit() and  int(user_message) < bot_num:
        bot.send_message(message.chat.id,'Я загадал число больше твоего')
    if  user_message.isdigit() and  int(user_message) > bot_num:
        bot.send_message(message.chat.id,'Я загадал число меньше твоего')
    if  user_message.isdigit() and  int(user_message) == bot_num:
        bot.send_message(message.chat.id,'Ты выйграл, сыграем еще?')

bot.polling()


