import datetime
import pprint
class FlightData:
    def __init__(self):
        self.fly_from = "LON"
        now = datetime.datetime.now()
        tomorrow = now + datetime.timedelta(days=1)
        six_months_ahead = now + datetime.timedelta(days=6*30)
        self.date_from = tomorrow.strftime("%d/%m/%Y")
        self.date_to = six_months_ahead.strftime("%d/%m/%Y")
        self.curr = "GBP"
        self.nights_in_dst_from = 7
        self.nights_in_dst_to = 28

    def create_query(self, code_to_city, stop_overs=0, via_city=""):
        query = {
            "fly_from": self.fly_from,
            "fly_to": code_to_city,
            "date_from": self.date_from,
            "date_to": self.date_to,
            "max_stopovers": stop_overs,
            "curr": self.curr,
            "nights_in_dst_from": self.nights_in_dst_from,
            "nights_in_dst_to": self.nights_in_dst_to,
            "flight_type": "round",
            "one_for_city": 1,
        }
        return query



