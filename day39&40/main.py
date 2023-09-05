from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()
users = data_manager.get_active_users()
ORIGIN_CITY_IATA = "LON"

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    if flight is not None and flight.price < destination["lowestPrice"]:
        pound = "£"

        if flight.stop_overs > 0:

            msg = (f"Low price alert! Only {pound}{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to"
                   f" {flight.destination_city}-{flight.destination_airport},"
                   f" from {flight.out_date} to {flight.return_date}.\n"
                   f"Flight has {flight.stop_overs} stop over, via {flight.via_city}")
        else:
            msg=f"Low price alert! Only {pound}{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."

        # notification_manager.send_sms(
        #     message=msg
        # )
        for user in users:
            notification_manager.send_email(message=msg, user=user)
