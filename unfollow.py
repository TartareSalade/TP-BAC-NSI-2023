from instabot import Bot
from time import sleep
from random import randint
import config

bot = Bot()
bot.login(username = config.username, password = config.password)
non_followers = set(bot.following) - set(bot.followers)
for non_follower in non_followers:
    try:
        bot.unfollow(non_followers)
        sleep(randint(6,12))
    except Exception as e:
        print(e)
        sleep(randint(30,300))