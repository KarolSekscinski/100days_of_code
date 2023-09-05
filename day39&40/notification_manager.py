import smtplib
# from twilio.rest import Client

TWILIO_SID = "ACb62dd2ce2e146d0dbd6b55d1bd204376"
TWILIO_AUTH_TOKEN = "7dbb5576c1b9e5b6d0d98107bfed42a5"
TWILIO_VIRTUAL_NUMBER = "+17622383481"
TWILIO_VERIFIED_NUMBER = "+48516844216"

MY_EMAIL = "karoltestemail@gmail.com"
MY_PASSWORD = "ziyvcqtldcebitne"

class NotificationManager:

    def __init__(self):
        pass
        # self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        print(message)
        # message = self.client.messages.create(
        #     body=message,
        #     from_=TWILIO_VIRTUAL_NUMBER,
        #     to=TWILIO_VERIFIED_NUMBER,
        # )
        # Prints if successfully sent.
        # print(message.sid)

    def send_email(self, message, user):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=user["email"],
                                msg=f"Subject: Hello {user['firstName']} {user['lastName']}\n\n{message}".encode("utf-8"))
