import os
from dotenv import load_dotenv
load_dotenv(verbose=True, dotenv_path='.env')


IS_SANDBOX = True if os.getenv('IS_TINKOFF_SANDBOX') == 'true' else False

BASE_HOST = 'https://api-invest.tinkoff.ru/openapi'

HOST = f'{BASE_HOST}/sandbox' if IS_SANDBOX else BASE_HOST
if IS_SANDBOX:
    TOKEN = os.getenv('TINKOFF_SANDBOX_TOKEN')
else:
    TOKEN = os.getenv('TINKOFF_TOKEN')
