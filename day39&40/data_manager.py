from pprint import pprint
import requests

SHEETY_PRICES_ENDPOINT = "YOUR ENDPOINT"
SHEETY_USERS_ENDPOINT = "YOUR ENDPOINT"
TOKEN = "YOUR TOKEN"
HEADERS = {
    "Authorization": TOKEN
}

class DataManager:

    def __init__(self):
        self.destination_data = {}
        self.users = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=HEADERS)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
                headers=HEADERS

            )
            print(response.text)

    def get_active_users(self):
        response = requests.get(url=SHEETY_USERS_ENDPOINT, headers=HEADERS)
        data = response.json()
        self.users = data["users"]
        return self.users

