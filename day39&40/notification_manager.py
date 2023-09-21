import smtplib
# from twilio.rest import Client

TWILIO_SID = "YOUR TWILIO SID"
TWILIO_AUTH_TOKEN = "YOUR TWILIO AUTH TOKEN"
TWILIO_VIRTUAL_NUMBER = "+YOUR TWILIO NUMBER"
TWILIO_VERIFIED_NUMBER = "+YOUR NUMBER"

MY_EMAIL = "YOUR EMAIL"
MY_PASSWORD = "YOUR PASSWORD"

class NotificationManager:

    def __init__(self):
        # self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
        pass


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
