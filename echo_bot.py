import telebot
import logging
import os
from app.app import get_interval_candles, get_volume, get_currency
from dotenv import load_dotenv
load_dotenv(verbose=True, dotenv_path='.env')

TOKEN = os.getenv('FINTECH_TOKEN')
bot = telebot.TeleBot(TOKEN, parse_mode='MARKDOWN')

keyboard_a = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard_a.row('/id', '/get_candles')


# @bot.channel_post_handler(commands=['id'])
@bot.message_handler(commands=['id'])
def send_id(message):
    bot.reply_to(message, f"`{message.chat.id}`", reply_markup=keyboard_a)


@bot.message_handler(commands=['get_candles'])
def get_ticker(message):
    if message.text.lower() == 'отмена':
        bot.send_message(message.from_user.id, 'На нетъ и суда нетъ')
        return
    if message.chat.username == 'danielle_kettler':
        ticker = bot.send_message(message.chat.id, 'give me a ticker')
        print(message.text)
        bot.register_next_step_handler(ticker, get_data)
    else:
        bot.reply_to(message, "who are you stranger?", reply_markup=keyboard_a)


def get_data(message):
    global ticker
    ticker = message.text.upper()
    if message.text.lower() == 'отмена':
        bot.send_message(message.from_user.id, 'На нетъ и суда нетъ')
        return
    send = bot.send_message(message.chat.id, 'give me date as\n'
                                             '2015-01-01 2016-02-02')
    bot.register_next_step_handler(send, interval_candle)


def interval_candle(message):
    left_date = str(message.text.split()[0])
    right_date = str(message.text.split()[1])

    print(ticker, left_date, right_date)

    res = get_interval_candles(ticker, left_date, right_date)
    bot.send_message(message.chat.id, res)


bot.polling()
