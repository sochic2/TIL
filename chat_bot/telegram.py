import requests
from bs4 import BeautifulSoup
import json
from pprint import pprint
import os

token = os.getenv("TELEGRAM_BOT_TOKEN")
method_name = "getUpdates"
url = f"https://api.telegram.org/bot{token}/{method_name}"
update = requests.get(url).json()

chat_id =  update["result"][0]["message"]["from"]["id"]

# print(chat_id)
method_name = "sendmessage"




nkospi = "https://finance.naver.com/sise/"
req_cos = requests.get(nkospi).text
soup = BeautifulSoup(req_cos, 'html.parser')
kospi = soup.select_one("#KOSPI_now").text

msg = f"코스피 지수 {kospi}"
msg_url = f"https://api.telegram.org/bot{token}/{method_name}?chat_id={chat_id}&text={msg}"

print(msg_url)
print(requests.get(msg_url))


