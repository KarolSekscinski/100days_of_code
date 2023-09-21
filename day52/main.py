from InstaFollower import InstaFollower
SIMILAR_ACCOUNT = "ekstraklasatrolls"
ACCOUNT_PAGE = "https://www.instagram.com/ekstraklasatrolls/"

follower_bot = InstaFollower(SIMILAR_ACCOUNT, ACCOUNT_PAGE)
follower_bot.login()
follower_bot.find_followers()
follower_bot.follow()

