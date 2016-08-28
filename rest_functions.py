import tweepy
import time
import json
#from keys import classes/functions and etc
from keys import *


#Sets up twitter authentication
auth = tweepy.OAuthHandler(consumer_key(), consumer_secret())
auth.set_access_token(access_token(), access_token_secret())
api = tweepy.API(auth)

#Returns list of tweet_objects of your own timeline
#public_tweets = api.home_timeline()

#keyword = "#"
#keyword += raw_input('Enter your hashtag: #')
#data = api.search(q=keyword)    #returns an array of tweet objects
#num_of_results = input('How many results do you want? ')    #Number of tweets we want
#numOfAttributes = 4     #Number of attributes we are tracking

#data = []
#processed_data = [[0 for i in xrange(numOfAttributes)] for i in xrange(num_of_results)]

#Adds all the tweets onto data *Each tweet is the json obj tweet
#FOR WHAT TO DOT OPERATE. LOOK AT TWITTER DOCUMENTATION FOR TWEETS.
#for tweet in tweepy.Cursor(api.search, q=keyword).items(num_of_results):
#        data.append(tweet)

def print_tweet(tweet):
    tweet_info = []
    tweet_info.append("@%s - %s (%s)" % (tweet.user.screen_name, tweet.user.name, tweet.created_at))
    tweet_info.append(tweet.text)
    tweet_info.append("Tweet coordinates: " + str(tweet.coordinates))
    tweet_info.append("Author Location: " + tweet.user.location)
    tweet_info.append("Retweet Count: " + str(tweet.retweet_count))
    return tweet_info
    #The dot operator allows for EASY dict-value getting

#process_data(data)
#for tweet in data:
#    print_tweet(tweet)
