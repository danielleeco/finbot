import requests
# from ratelimit import limits, sleep_and_retry
import logging

from .auth import HOST, TOKEN
ONE_MINUTE = 60


def get_figi_by_ticker(ticker: str):
    url = f'{HOST}/market/search/by-ticker'
    headers = {
        'Authorization': f'Bearer {TOKEN}',
        'Accept': 'application/json',
    }
    params = {
        'ticker': ticker
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        insts = response.json()['payload']['instruments']
        if len(insts) != 1:
            raise Exception(f"insts by ticker {len(insts)}")
        figi = insts[0]['figi']
    except Exception:
        logging.error(response.json())
        return None
    return figi


def get_candles(ticker: str, left_time: str, right_time: str, interval='day'):
    figi = get_figi_by_ticker(ticker)
    url = f'{HOST}/market/candles'
    headers = {
        'Authorization': f'Bearer {TOKEN}',
        'Accept': 'application/json',
    }

    left_time += 'T12:00:00.131642+03:00'
    right_time += 'T12:00:00.131642+03:00'

    params = {
        'figi': figi,
        'from': left_time,
        'to': right_time,
        'interval': interval
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        candles = response.json()['payload']['candles']
    except Exception:
        logging.error(response.json())
        return None
    return candles


def get_interval_candles(ticker: str, left_time: str,
                         right_time: str, interval='day'):
    left_time_1 = left_time[:-1] + str(int(left_time[-1]) - 1)
    right_time_1 = right_time[:-1] + str(int(right_time[-1]) - 1)
    left_time_2 = left_time
    right_time_2 = right_time

    start = get_candles(ticker, left_time_1, left_time_2, interval='day')
    end = get_candles(ticker, right_time_1, right_time_2, interval='day')

    res = [start[0]['o'], end[0]['o']]
    diff = round(100 - (100 / (res[0] / res[1])), 2)
    result = f'Ticker - {ticker}: {left_time} {res[0]}$ - {right_time} {res[1]}$ diff {diff}%'
    return result
