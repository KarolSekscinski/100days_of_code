##################### Extra Hard Starting Project ######################
import smtplib
import datetime as dt
import random as r
import pandas as pd

MY_EMAIL = "karoltestemail@gmail.com"
MY_PASSWORD = "ziyvcqtldcebitne"


data = pd.read_csv("birthdays.csv")

birthday_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}

current_day = dt.datetime.now().day
current_month = dt.datetime.now().month
today = (current_month, current_day)

if today in birthday_dict:
    file_path = f"letter_templates/letter_{r.randint(1,3)}.txt"
    someone_email = birthday_dict[today]["email"]
    someone_name = birthday_dict[today]["name"]

    with open(file_path) as file:
        actual_letter = file.read()

    letter = actual_letter.replace("[NAME]", someone_name)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=someone_email,
                            msg=f"Subject: Happy Birthday {someone_name}\n\n{letter}")






