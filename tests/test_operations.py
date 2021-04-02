from app.app import get_figi_by_ticker, get_candles


def test_tesla_ticker():
    ticker = 'TSLA'
    assert get_figi_by_ticker(ticker) == 'BBG000N9MNX3', 'Unexpected figi'
    # it may change one daypython -m pytest


def test_data_candels():
    ticker = 'TSLA'
    assert get_candles(ticker, '2019-03-12', '2019-05-12') == 'N9MNX3', '2'
