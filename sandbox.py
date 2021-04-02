from app.app import get_figi_by_ticker, get_candles, get_interval_candles

def test_data_candles():
    ticker = 'TSLA'
    print(get_interval_candles(ticker, '2019-03-12', '2019-08-12'))

test_data_candles()

# s = '2019-08-19'
# sn = s[:-1] + str(int(s[-1]) - 1)

# print(sn)

# exp = [[{'o': 58.29, 'c': 56.5, 'h': 58.374, 'l': 56.22, 'v': 9841365, 'time': '2019-03-12T07:00:00Z', 'interval': 'day', 'figi': 'BBG000N9MNX3'}], 
# [{'o': 46.92, 'c': 45.832, 'h': 47.382, 'l': 45.764, 'v': 5881495, 'time': '2019-08-12T07:00:00Z', 'interval': 'day', 'figi': 'BBG000N9MNX3'}]]
# print(exp[0][0]['o'])
# print(exp[1][0]['o'])