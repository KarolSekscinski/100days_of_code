import requests
from bs4 import BeautifulSoup
import smtplib

MY_EMAIL = "karoltestemail@gmail.com"
MY_PASSWORD = "ziyvcqtldcebitne"

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
                            to_addrs="socer404@gmail.com",
                            msg=f"Subject: Hello Karol\n\n{message}".encode("utf-8"))








# HEADERS = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
#     "sec-fetch-site": "cross-site",
#     "sec-fetch-mode": "navigate",
#     "sec-fetch-user": "?1",
#     "sec-fetch-dest": "document",
#     "sec-ch-ua": '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
#     "sec-ch-ua-mobile": "?0",
#     "sec-ch-ua-platform": "Windows",
#     "Accept-Encoding": "gzip, deflate, br",
#     "Accept-Language": "pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7,en-GB;q=0.6",
#     "Cookie": "PHPSESSID=aa1e6cf512b34006adfeee81f779a0cb",
#     "x-forwarded-proto": "https",
#     "x-https": "on",
#     "X-Forwarded-For": "109.231.4.200",
# }
# response = requests.get(url=URL, headers=HEADERS)
# webpage = response.text
# pprint(webpage)
# soup = BeautifulSoup(webpage, "html.parser")
# price = soup.find(name="span", class_="a-price-whole")
# print(price)