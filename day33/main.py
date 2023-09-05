import requests
from datetime import datetime
MY_LAT = 53.096519
MY_LNG = 23.118393
# URL_ISS = "http://api.open-notify.org/iss-now.json"
#
# response = requests.get(url=URL)
# response.raise_for_status()
#
# data = response.json()
#
# longitude = data["iss_position"]['longitude']
# latitude = data['iss_position']['latitude']
#
# iss_position = (longitude, latitude)
# print(iss_position)
URL_SUNSET = "https://api.sunrise-sunset.org/json"
parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,
}

response = requests.get(url=URL_SUNSET, params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data['results']['sunrise'].split("T")[1].split(":")[0]
sunset = data['results']['sunset'].split("T")[1].split(":")[0]
print(sunset)
print(sunrise)
time_now = datetime.now()
