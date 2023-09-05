import smtplib
import datetime as dt
import random as r

my_email = "karoltestemail@gmail.com"
my_password = "ziyvcqtldcebitne"
other_password = "kfrrrmguqxluaytg"
second_email = "testkarolemail@gmail.com"


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

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=second_email, password=other_password)
#     connection.sendmail(from_addr=second_email,
#                         to_addrs=my_email,
#                         msg="Subject:Hello there\n\nHello world")


