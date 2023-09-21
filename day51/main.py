from InternetSpeedTwitterBot import InternetSpeedTwitterBot

PROMISED_DOWN = 100
PROMISED_UP = 30
TWITTER_EMAIL = "YOUR TWITTER EMAIL"
TWITTER_PASSWORD = "YOUR TWITTER PASSWORD"
URL = "https://twitter.com"
SPEED_TEST_URL = "https://www.speedtest.pl/"

bot = InternetSpeedTwitterBot(url=SPEED_TEST_URL, up=PROMISED_UP, down=PROMISED_DOWN)
internet_speed = bot.get_internet_speed()
tweet = bot.tweet_at_provider()



