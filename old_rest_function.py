import tweepy
import time
import json
#from keys import classes/functions and etc
from keys import *


#Sets up twitter authentication
auth = tweepy.OAuthHandler(consumer_key(), consumer_secret())
auth.set_access_token(access_token(), access_token_secret())
api = tweepy.API(auth)

def print_tweet(tweet):
    tweet_info = []
    tweet_info.append("@%s - %s (%s)" % (tweet.user.screen_name, tweet.user.name, tweet.created_at))
    tweet_info.append(tweet.text)
    tweet_info.append("Tweet coordinates: " + str(tweet.coordinates))
    tweet_info.append("Author Location: " + tweet.user.location)
    tweet_info.append("Retweet Count: " + str(tweet.retweet_count))
    tweet_info.append("Retweeted: " + str(tweet.retweeted))
    tweet_info.append("Phone Type: " + str(tweet.source))
    #tweet_info.append("Sensitive: " + str(tweet.possibly_sensitive))
    tweet_info.append("Language: " + str(tweet.lang))
    return tweet_info
    #The dot operator allows for EASY dict-value getting

#process_data(data)
#for tweet in data:
#    print_tweet(tweet)
