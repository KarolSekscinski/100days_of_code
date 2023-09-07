from bs4 import BeautifulSoup
import requests

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(url=URL)
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")

greatest_films = soup.find_all(name="h3", class_="title")
with open("./movies.txt", mode="a", encoding="utf-8") as file:
    for film in greatest_films[::-1]:

        file.write(f"{film.text}\n")

