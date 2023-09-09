from InternetSpeedTwitterBot import InternetSpeedTwitterBot

PROMISED_DOWN = 100
PROMISED_UP = 30
TWITTER_EMAIL = "KComplain28815"
TWITTER_PASSWORD = "u#D6w,/i#U:6-an"
URL = "https://twitter.com"
SPEED_TEST_URL = "https://www.speedtest.pl/"

bot = InternetSpeedTwitterBot(url=SPEED_TEST_URL, up=PROMISED_UP, down=PROMISED_DOWN)
internet_speed = bot.get_internet_speed()
tweet = bot.tweet_at_provider()



