import requests
from twilio.rest import Client
URL = "https://api.openweathermap.org/data/3.0/onecall"

API_KEY = "YOUR API KEY"
ACCOUNT_SID = "YOUR ACCOUNT SID"
AUTH_TOKEN = "YOUR AUTH TOKEN"

MY_LAT = 0
MY_LONG = 0

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
    "exclude": "current,minutely,daily"
}

response = requests.get(url=URL, params=parameters)
response.raise_for_status()

data = response.json()
weather_data = data["hourly"]
should_take_umbrella = False
weather_slice = weather_data[:12]
for weather in weather_slice:
    condition_code = weather["weather"][0]["id"]

    if condition_code < 700:
        should_take_umbrella = True

if should_take_umbrella:
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages \
        .create(
                body="It's going to rain today. Remember to bring an umbrella☂️ :)",
                from_='+YOUR NUMBER',
                to='+YOUR NUMBER'
                )
print(message.status)

