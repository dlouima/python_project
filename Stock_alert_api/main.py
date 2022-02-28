from datetime import datetime
from twilio.rest import Client
import os
import requests
from dotenv import load_dotenv
load_dotenv()

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get('AUTH_TOKEN')
apikey = os.getenv("API_KEY")

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": apikey
}

response = requests.get(STOCK_ENDPOINT, params=parameters)
data = response.json()["Time Series (Daily)"]

data_to_list = [value for (key, value) in data.items()]
yesterday_closing = float(data_to_list[0]['4. close'])

before_yesterday_closing = float(data_to_list[1]['4. close'])

print(before_yesterday_closing)
print(yesterday_closing)

change = abs(round(yesterday_closing - before_yesterday_closing, 2))
print(change)
change_percentage = round(change/yesterday_closing*100, 2)
print(change_percentage)

if change_percentage > 1:

    news_api_key = os.getenv("NEWS_API_KEY")
    q = 'tesla'
    Date = datetime.now().date()
    print(Date)
    publisher = 'publishedAt'
    news_parms = {
        'q': q,
        'from': data,
        'sortBy': publisher,
        'apiKey': news_api_key}

    news = requests.get(url=NEWS_ENDPOINT, params=news_parms)
    news_data = news.json()['articles'][:3]

    news_list = [
        f"Headline:{article['title']}. \n Brief: {article['description']}" for article in news_data]

    client = Client(account_sid, auth_token)
    for article in news_list:
        message = client.messages.create(
            body=article, from_='+12356899615', to='+13695829683')
        print(message.status)
