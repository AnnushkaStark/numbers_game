import telebot 
import random
bot = telebot.TeleBot('6029515865:AAGYMP9S2QjY3e69ekjkHClJnOmziEhMiTY')
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,'Привет, поиграем в угадай число')
    bot.send_message(message.chat.id,'Я загадаю число от 1 до 100 попробуй его угадать')
    bot.send_message(message.chat.id,'Введите число от 1 до 100')
    
@bot.message_handler(func= lambda message:True)
def get_text_message(message):
    bot_num  = random.randint(1,100)
    user_message = message.text.lower()
    user_num = int(user_message)
   
    if 1 > user_num > 100:
        bot.send_message(message.chat.id,'А может все таки число от 1 го до 100')
    elif user_num < bot_num:
        bot.send_message(message.chat.id,'Я загадал число больше твоего')
    elif user_num > bot_num:
        bot.send_message(message.chat.id,'Я загадал число меньше твоего')
    elif user_num == bot_num:
        bot.send_message(message.chat.id,'Ты выйграл, сыграем еще?')

bot.polling()


