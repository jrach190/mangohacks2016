


#import the tweepy library for twitter python, can be found at https://github.com/tweepy/tweepy
import tweepy
from tweepy import OAuthHandler
from DatumBox import DatumBox

API_KEY = "454ec357b72e7d0c06cac8df90bb8862"



ckey = 'U9Tafmmex2480HX7rk0WBlxVz'
csecret = 'j12CT89zB9kac8NnVVyP9C75NLxoijvfpGIpR5HwxPOf2Tj9pr'
atoken = '213110253-Iz7sSME8PDW9qvKaueDkvEKzzsCPS40LQhzGM2cW'
asecret = 'Ctl89F53FPNjgLq9wThS2ZZXop4OT15DMe5v0IwGdMI7K'
user = raw_input("enter the handle of who you want\n")

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
api = tweepy.API(auth)

datum_box = DatumBox(API_KEY)

list = []

for status in api.user_timeline(user, count = 10):
    list.append(str(status.text))
    print status.text
for tweet in list:
    for word in tweet:
        word.replace("@","")
    print "Converted string is: %s" % tweet
    tweet = datum_box.twitter_sentiment_analysis(tweet)
    print tweet

