from bs4 import BeautifulSoup
import requests


response = requests.get("https://news.ycombinator.com/news")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")

articles = soup.find_all(name="span", class_="titleline")
article_texts = []
article_links = []

for article in articles:
    article_texts.append(article.text.split(" (")[0])
    article_links.append(article.find("a").get("href"))


articles_upvote = [int(score.text.split(" ")[0]) for score in soup.find_all(name="span", class_="score")]

# print(article_texts)
# print(article_links)
# print(articles_upvote)

highest_score_index = articles_upvote.index(max(articles_upvote))
print(article_texts[highest_score_index])
print(article_links[highest_score_index])
