import requests

SHEETY_ENDPOINT = "https://api.sheety.co/220463ab263c7c42fd4fbaad8577ec39/flightFinder/prices"
TOKEN = "Bearer LSDKANDASHGDUIAlansdasndasdasdasdnmxczbgi"
HEADERS = {
    "Authorization": TOKEN
}
class DataManager:
    def __init__(self):
        # self.sheety_endpoint = "https://api.sheety.co/220463ab263c7c42fd4fbaad8577ec39/flightFinder/prices"
        # self.token = "Bearer LSDKANDASHGDUIAlansdasndasdasdasdnmxczbgi"
        self.response = None
        self.prices = None

    def return_prices(self):
        self.response = requests.get(url=SHEETY_ENDPOINT, headers=HEADERS)
        self.prices = self.response.json()["prices"]
        return self.prices

    def update_iatacode(self, row_data):
        row_id = row_data["id"]
        request_body = {
            "price": {
                "iataCode": row_data["iataCode"],
            }
        }
        self.response = requests.put(url=f"{SHEETY_ENDPOINT}/{row_id}", headers=HEADERS, json=request_body)
        print(self.response.text)










