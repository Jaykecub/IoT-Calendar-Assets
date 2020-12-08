import twitter
import json
import sys
import tweepy 
from tweepy.auth import OAuthHandler


CONSUMER_KEY = ''
CONSUMER_SECRET= ''
OAUTH_TOKEN=''
OAUTH_TOKEN_SECRET = ''

auth = twitter.OAuth(OAUTH_TOKEN,OAUTH_TOKEN_SECRET,CONSUMER_KEY,CONSUMER_SECRET)


twitter_api =twitter.Twitter(auth=auth)

print twitter_api

statuses = twitter_api.statuses.user_timeline(screen_name='@realDonaldTrump')
print [status['text'] for status in statuses]