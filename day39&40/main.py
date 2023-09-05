#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.return_prices()
flight_data = FlightData()
for row in sheet_data:

    if row["iataCode"] == "":
        flight_search = FlightSearch()
        iata_code = flight_search.find_iatacode(city_name=row["city"])
        row["iataCode"] = iata_code
        data_manager.update_iatacode(row_data=row)
    else:
        flight_search = FlightSearch()
        data = flight_search.find_lowest_price(city_code=row["iataCode"])
        if data is None:
            continue
        else:
            price = data['price']
            if row['lowestPrice'] > price:
                notification_manager = NotificationManager()
                notification_manager.sent_message(data)




