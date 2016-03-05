from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

ckey = 'U9Tafmmex2480HX7rk0WBlxVz'
csecret = 'j12CT89zB9kac8NnVVyP9C75NLxoijvfpGIpR5HwxPOf2Tj9pr'
atoken = '213110253-Iz7sSME8PDW9qvKaueDkvEKzzsCPS40LQhzGM2cW'
asecret = 'Ctl89F53FPNjgLq9wThS2ZZXop4OT15DMe5v0IwGdMI7K'

class listener(StreamListener):

	def on_data(self, data):
		saveFile = open('twitDb.csv','a')
		saveFile.write(data)
		saveFile.write('\n')
		saveFile.close()
		
		tweet = data.split(',"text":"')[1]
		tweet = tweet.split('","source":"')[0]
		time = data.split
		print (tweet)
		return True
	
	def on_error(self, status):
		print (status)
		

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=["cat"])
