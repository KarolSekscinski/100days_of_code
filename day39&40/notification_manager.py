ACCOUNT_SID = "ACb62dd2ce2e146d0dbd6b55d1bd204376"
AUTH_TOKEN = "7dbb5576c1b9e5b6d0d98107bfed42a5"

from twilio.rest import Client


class NotificationManager:
    def __init__(self):
        pass

    def sent_message(self, data):
        client = Client(ACCOUNT_SID, AUTH_TOKEN)
        price = data['price']
        departure_city_name = data['cityFrom']
        departure_iata_code = data['flyFrom']
        arrival_city_name = data['cityTo']
        arrival_iata_code = data['flyTo']
        outbound_date = data['local_departure'].split("T")
        inbound_date = data['local_arrival'].split("T")
        msg = f"Low price alert! Only £{price} to fly from {departure_city_name}-{departure_iata_code} to {arrival_city_name}-{arrival_iata_code}, from {outbound_date[0]} to {inbound_date[0]}."
        print(msg)
        # message = client.messages.create(
        #     body=msg,
        #     from_='+17622383481',
        #     to='+48516844216'
        # )
        # print(message.status)