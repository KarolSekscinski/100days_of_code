import requests
import datetime as dt
import os
print(os.environ)
APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]
print(APP_ID)

exercise_endpoint = os.environ["exercise_endpoint"]
token = os.environ["token"]

sheety_endpoint = os.environ["sheety_endpoint"]
# APP_ID = "ba6d209c"
# API_KEY = "7a75745a57db1bf2257b963e4cc2b8ce"
#
#
# exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
# token = "Bearer SAJDONASKDANSLDNaohsdoasndaskd"
#
# sheety_endpoint = "https://api.sheety.co/220463ab263c7c42fd4fbaad8577ec39/workingTracking/workouts"
GENDER = "male"
WEIGHT_KG = 77.0
HEIGHT = 180.0
AGE = 21

user_exercise = input("Tell me which exercises you did:")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

parameters = {
    "query": user_exercise,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT,
    "age": AGE
}

response = requests.post(url=exercise_endpoint, headers=headers, json=parameters)
data = response.json()
user_data = data["exercises"][0]

date = dt.datetime.now().strftime("%d/%m/%Y")
time = dt.datetime.now().strftime("%X")

exercise = user_data["name"].title()
duration = round(user_data["duration_min"])
calories = round(user_data["nf_calories"])

sheety_headers = {
    "Authorization": token
}

sheety_body = {
    "workout": {
        "date": date,
        "time": time,
        "exercise": exercise,
        "duration": duration,
        "calories": calories
    }
}
sheety_response = requests.post(url=sheety_endpoint, json=sheety_body, headers=sheety_headers)

print(sheety_response.text)
