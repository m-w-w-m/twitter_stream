from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

ckey = 'H237cHGshuhFS6dPQwsAVET8G'
csecret = 'vtlY6yL6yEzXZPCdZIVEygzQgo0MfXdHoZJgOwhpoFlK4m7Jky'
atoken = '1088394379784581122-8NyGV4uTQ4iN7SheocJ5d0uaZ9qhvt'
asecret = 'vIUL6pXX3aZTKJ5wYJRxhqjqCiI0L0uw1jgGYLL24EcTV'

class Listener(StreamListener):

	def on_data(self, data):
		print(data)
		return True

	def on_error(self, status):
		print(status)


auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, Listener())
twitterStream.filter(track=["road"])