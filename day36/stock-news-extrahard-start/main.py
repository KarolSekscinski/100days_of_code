import requests
from twilio.rest import Client

# STOCK MARKET
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = "ZR45DJ8OKVH0FQ12"
# NEWS
NEWS_API_KEY = "a623625f19bb4582b7761c3bdbf17a08"
# SMS
ACCOUNT_SID = "ACb62dd2ce2e146d0dbd6b55d1bd204376"
AUTH_TOKEN = "7dbb5576c1b9e5b6d0d98107bfed42a5"
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


# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

response = requests.get(url=URL_STOCK, params=stock_parameters)
data = response.json()['Time Series (Daily)']
data_list = [value for (key, value) in data.items()]
# Closing data for stock market
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

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

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

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.



#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

