import requests
from bs4 import BeautifulSoup
import smtplib

MY_EMAIL = "YOUR EMAIL"
MY_PASSWORD = "YOUR PASSWORD"

URL = "https://sprzedajemy.pl/drukarka-laserowa-lexmark-4062-41a-mono-pszczyna-2-0010c9-nr66152662"

response = requests.get(url=URL)

cookies = response.cookies

response = requests.get(url=URL, cookies=cookies)
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")
price_text = soup.find(name="strong", class_="price")
price = float(price_text.text.split(" ")[0])
if price < 250:
    message = f"Super oferta kupna drukarki za jedyne {price} zl Link:{URL}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs="YOUR SECOND EMAIL",
                            msg=f"Subject: Hello Karol\n\n{message}".encode("utf-8"))

