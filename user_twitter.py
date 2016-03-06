"""Created by Jonathan Rach, Sean Holden, and AJ Hinsvark for MangoHacks2016"""
"""This code is designed to take input from website, run sentiment analysis on tweets from desired user, and return tweets and mood"""
"""to the front end for display to the user. Built using the Tweepy, DatumBox, and Flask libraries and API's."""


#import the tweepy library for twitter python, can be found at https://github.com/tweepy/tweepy
import tweepy
from tweepy import OAuthHandler
from DatumBox import DatumBox
from flask import Flask
from flask import request
from flask import render_template



API_KEY = "454ec357b72e7d0c06cac8df90bb8862"

app=Flask(__name__)



ckey = 'U9Tafmmex2480HX7rk0WBlxVz'
csecret = 'j12CT89zB9kac8NnVVyP9C75NLxoijvfpGIpR5HwxPOf2Tj9pr'
atoken = '213110253-Iz7sSME8PDW9qvKaueDkvEKzzsCPS40LQhzGM2cW'
asecret = 'Ctl89F53FPNjgLq9wThS2ZZXop4OT15DMe5v0IwGdMI7K'

#user = '@elonmusk'
#user = raw_input("enter the handle of who you want\n")

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
api = tweepy.API(auth)

datum_box = DatumBox(API_KEY)

@app.route('/',methods=['POST','GET'])
def home():
    return render_template('/index.html')


def miapp():
    user_name = request.form['user']
    
    if user_name=="":
        return render_template('index.html')
    
    tweetlist = []
    sentlist = []

    # print u"Mystery char: \u2026"
    # print type("\u2026")

    # For each status, clean up the tweet itself and get the sentiment
    for status in api.user_timeline(user_name, count = 10):

        # Declare empty cleaned tweet string
        cleantweet = ''

        # Clean up - anything non-alphanumeric in the tweet text is useless
        # and can potentially cause an error with the datumbox call
        for char in status.text:
            if char.isalnum() or char.isspace():
                cleantweet += char


        tweetlist.append(cleantweet)
        sentiment = datum_box.twitter_sentiment_analysis(cleantweet)

        sentlist.append(sentiment)

        #print ("Sentiment is \"{0}\" for tweet \"{1}\"".format(sentiment, cleantweet))


    #for i in tweetlist:
    #       print i
    #   for i in sentlist:
    #       print i
    return render_template('index.html')

if __name__ == "__main__":
    app.run()