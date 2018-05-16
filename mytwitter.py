import tweepy
from textblob import TextBlob

consumer_key = 'Your Key'
consumer_secret = 'Your Key'

access_token = 'Your Token'
access_token_secret = 'YOur Token'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

public_tweet = api.search('Your Key word')

for tweet in public_tweet:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)