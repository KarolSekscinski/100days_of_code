import requests
from twilio.rest import Client
URL = "https://api.openweathermap.org/data/3.0/onecall"
# This should be env variables v
API_KEY = "1a54b8230c7cddc9591781028cc63068"
ACCOUNT_SID = "ACb62dd2ce2e146d0dbd6b55d1bd204376"
AUTH_TOKEN = "7dbb5576c1b9e5b6d0d98107bfed42a5"
# This should be env variables ^
MY_LAT = 53.561316
MY_LONG = -68.521729

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
                from_='+17622383481',
                to='+48516844216'
                )
print(message.status)

