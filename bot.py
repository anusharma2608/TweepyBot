import tweepy
from time import sleep
from credentials import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

QUERY = 'Python'
LIKE = True
FOLLOW = True
SLEEP_TIME = 300000


print("Twitter bot which retweets, like tweets and follow users")
print("Bot Settings")
print("Like Tweets :", LIKE)
print("Follow users :", FOLLOW)

for tweet in tweepy.Cursor(api.search_tweets, q = QUERY).items():
	try:
		print('\nTweet by: @' + tweet.user.screen_name)

		tweet.retweet()
		print('Retweeted the tweet')

		if LIKE:
			tweet.favorite()
			print('Favorited the tweet')

		if FOLLOW:
			if not tweet.user.following:
				tweet.user.follow()
				print('Followed the user')

		sleep(SLEEP_TIME)

	except AttributeError as e:
		print(e.reason)

	except StopIteration:
		break

