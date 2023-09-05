import requests
from flight_data import FlightData
from pprint import pprint
# This class is responsible for talking to the Flight Search API.

TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com"
TEQUILA_LOCATIONS = "/locations/query"
TEQUILA_SEARCH = "/v2/search"
API_KEY = "ePnp2v6i5t-4IUH4im1EqdBxcRdNMfqw"
class FlightSearch:
    def __init__(self):
        # self.flight_search_endpoint = "https://api.tequila.kiwi.com/locations/query"
        # self.apikey = "ePnp2v6i5t-4IUH4im1EqdBxcRdNMfqw"
        self.response = None
        self.results = None

    def find_iatacode(self, city_name):

        request_header = {
            "apikey": API_KEY,


        }
        request_body = {
            "term": city_name,
            "location_types": "city",
        }
        url = TEQUILA_ENDPOINT + TEQUILA_LOCATIONS
        self.response = requests.get(url=url, headers=request_header, params=request_body)

        results = self.response.json()["locations"]
        code = results[0]["code"]
        return code

    def find_lowest_price(self, city_code):
        flight_data = FlightData()
        request_header = {
            "apikey": API_KEY,

        }

        request_parameters = flight_data.create_query(city_code)
        url = TEQUILA_ENDPOINT + TEQUILA_SEARCH
        self.response = requests.get(url=url, headers=request_header, params=request_parameters)
        try:
            data = self.response.json()['data'][0]
        except IndexError:
            body = flight_data.create_query(city_code, stop_overs=2)
            url_stop_overs2 = TEQUILA_ENDPOINT + TEQUILA_SEARCH
            response = requests.get(url=url_stop_overs2, headers=request_header, params=body)

            pprint(response.json()['data'][0])
        else:
            self.results = data
        finally:
            return self.results

