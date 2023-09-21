import smtplib
import datetime as dt
import random as r

my_email = "YOUR EMAIL"
my_password = "YOUR PASSWORD"
other_password = "YOUR PASSWORD"
second_email = "YOUR EMAIL"


if dt.datetime.now().weekday() == 4:
    with open("motivational_mail/quotes.txt", mode="r") as file:
        message = r.choice(file.readlines())
        message = "Subject:Daily Motivation\n\n" + message
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=second_email,
                            msg=message)




