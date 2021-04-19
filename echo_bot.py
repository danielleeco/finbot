import telebot
import os
from app.app import get_interval_candles, get_volume, get_currency
from dotenv import load_dotenv
load_dotenv(verbose=True, dotenv_path='.env')

TOKEN = os.getenv('FINTECH_TOKEN')
bot = telebot.TeleBot(TOKEN, parse_mode='MARKDOWN')

keyboard_a = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard_a.row('/get_candles', '/get_volume', '/get_currency')

valid_logins = ('danielle_kettler', 'BarinovAF')

# @bot.channel_post_handler(commands=['start'])
@bot.message_handler(commands=['start'])
def send_id(message):
    bot.reply_to(message, "Hello", reply_markup=keyboard_a)

# get candles handler
@bot.message_handler(commands=['get_candles'])
def get_ticker(message):
    if message.text.lower() == 'отмена':
        bot.send_message(message.from_user.id, 'На нетъ и суда нетъ')
        return
    if message.chat.username in valid_logins:
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
                                             '2017-03-14 2019-10-22')
    bot.register_next_step_handler(send, interval_candle)


def interval_candle(message):
    left_date = str(message.text.split()[0])
    right_date = str(message.text.split()[1])

    print(ticker, left_date, right_date)

    res = get_interval_candles(ticker, left_date, right_date)
    bot.send_message(message.chat.id, res)



# get volume handler
@bot.message_handler(commands=['get_volume'])
def get_ticker2(message):
    if message.text.lower() == 'отмена':
        bot.send_message(message.from_user.id, 'На нетъ и суда нетъ')
        return
    if message.chat.username in valid_logins:
        ticker = bot.send_message(message.chat.id, 'give me a ticker')
        print(message.text)
        bot.register_next_step_handler(ticker, get_data2)
    else:
        bot.reply_to(message, "who are you stranger?", reply_markup=keyboard_a)


def get_data2(message):
    global ticker
    ticker = message.text.upper()
    if message.text.lower() == 'отмена':
        bot.send_message(message.from_user.id, 'На нетъ и суда нетъ')
        return
    send = bot.send_message(message.chat.id, 'give me date as\n'
                                             '2017-08-23')
    bot.register_next_step_handler(send, interval_vol)


def interval_vol(message):
    date = str(message.text.split()[0])

    print(ticker, date)

    res = get_volume(ticker, date)
    bot.send_message(message.chat.id, res)


# get currency handler
@bot.message_handler(commands=['get_currency'])
def get_curr(message):
    if message.text.lower() == 'отмена':
        bot.send_message(message.from_user.id, 'На нетъ и суда нетъ')
        return
    if message.chat.username in valid_logins:
        curr = bot.send_message(message.chat.id, 'give me name of a currency')
        print(message.text)
        bot.register_next_step_handler(curr, get_data3)
    else:
        bot.reply_to(message, "who are you stranger?", reply_markup=keyboard_a)


def get_data3(message):
    global curr
    curr = message.text.upper()
    if message.text.lower() == 'отмена':
        bot.send_message(message.from_user.id, 'На нетъ и суда нетъ')
        return
    send = bot.send_message(message.chat.id, 'give me date as\n'
                                             '2019-03-12 2019-02-26')
    bot.register_next_step_handler(send, interval_curr)


def interval_curr(message):
    left_date = str(message.text.split()[0])
    right_date = str(message.text.split()[1])

    print(curr, left_date, right_date)

    res = get_currency(curr, left_date, right_date)
    bot.send_message(message.chat.id, res)


bot.polling()
