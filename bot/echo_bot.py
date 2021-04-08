import telebot
import logging
import os
from query import query

# from dotenv import load_dotenv
# load_dotenv(verbose=True, dotenv_path='.env')

# TOKEN = os.getenv('FINTECH_TOKEN')
bot = telebot.TeleBot('1715795826:AAETECGhgM-XpU4Q1b79wsI7YR_s2VuDdpI')  # You can set parse_mode by default. HTML or MARKDOWN

# # @bot.channel_post_handler(func=lambda m: True)
# @bot.message_handler(func=lambda m: True)
# def echo_all(message):
#     logging.error(message)
#     bot.reply_to(message, message.text)


keyboard_a = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard_a.row('/whoami', '/id')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет',
                     reply_markup=keyboard_a)


# @bot.channel_post_handler(commands=['id'])
@bot.message_handler(commands=['id'])
def send_id(message):
    bot.reply_to(message, f"`{message.chat.id}`", reply_markup=keyboard_a)


# @bot.channel_post_handler(commands=['id'])
@bot.message_handler(commands=['whoami'])
def send_id(message):
    if message.chat.username == 'danielle.kettler':
        request = query('artists')[:30]
        request = [str(i) for i in request]
        req = '\n'.join(request)
        bot.send_message(message.chat.id, req, reply_markup=keyboard_a)

    else: bot.reply_to(message, "who are you stranger?", reply_markup=keyboard_a)


bot.polling()
