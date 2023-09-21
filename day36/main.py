import requests
from twilio.rest import Client

# STOCK MARKET
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = "YOUR API KEY"
# NEWS
NEWS_API_KEY = "YOUR API KEY"
# SMS
ACCOUNT_SID = "YOUR ACCOUNT SID"
AUTH_TOKEN = "YOUR AUTH TOKEN"
URL_STOCK = "https://www.alphavantage.co/query"
URL_NEWS = "https://newsapi.org/v2/everything"
increase_symbol = "🔺"
decrease_symbol = "🔻"

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY
}

news_parameters = {
    "apiKey": NEWS_API_KEY,
    "q": COMPANY_NAME,
}

response = requests.get(url=URL_STOCK, params=stock_parameters)
data = response.json()['Time Series (Daily)']
data_list = [value for (key, value) in data.items()]

yesterday_closing = float(data_list[0]["4. close"])
day_before_closing = float(data_list[1]["4. close"])

stock_price_change = yesterday_closing - day_before_closing
stock_price_percent = (stock_price_change / yesterday_closing) * 100
stock_price_percent = round(stock_price_percent)

if stock_price_percent > 0:
    stock_message = f"{STOCK}: {increase_symbol} {abs(stock_price_percent)}%"
else:
    stock_message = f"{STOCK}: {decrease_symbol} {abs(stock_price_percent)}%"
print(stock_message)


if abs(stock_price_percent) >= 1:
    response = requests.get(url=URL_NEWS, params=news_parameters)
    data = response.json()['articles']
    last_3_articles = data[:3]
    articles_msg = [f"{stock_message}\nHeadline: {article['title']}\nBrief:{article['description']}"
                    for article in last_3_articles]
    print(articles_msg)
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    for msg in articles_msg:
        message = client.messages.create(
                body=msg,
                from_='+17622383481',
                to='+48516844216'
            )
print(message.status)


