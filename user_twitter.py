import tweepy
from tweepy import OAuthHandler

ckey = 'U9Tafmmex2480HX7rk0WBlxVz'
csecret = 'j12CT89zB9kac8NnVVyP9C75NLxoijvfpGIpR5HwxPOf2Tj9pr'
atoken = '213110253-Iz7sSME8PDW9qvKaueDkvEKzzsCPS40LQhzGM2cW'
asecret = 'Ctl89F53FPNjgLq9wThS2ZZXop4OT15DMe5v0IwGdMI7K'
user = '@elonmusk'

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
api = tweepy.API(auth)

# print(api.user_timeline(user).text)

for status in api.user_timeline(user, count=10):
    print(status.text)
