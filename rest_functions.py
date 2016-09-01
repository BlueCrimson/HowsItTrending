import tweepy
import time
import json
#from keys import classes/functions and etc
from keys import *


#Sets up twitter authentication
auth = tweepy.OAuthHandler(consumer_key(), consumer_secret())
auth.set_access_token(access_token(), access_token_secret())
api = tweepy.API(auth)

def get_tweets(listOfTweets, keyword, numOfTweets):
    for tweet in tweepy.Cursor(api.search, q=keyword).items(numOfTweets):
        listOfTweets.append({'Screen Name': tweet.user.screen_name})
        listOfTweets.append({'User Name': tweet.user.name})
        listOfTweets.append({'Tweet Created At': unicode(tweet.created_at)})
        listOfTweets.append({'Tweet Text': tweet.text})
        listOfTweets.append({'User Location': unicode(tweet.user.location)})
        listOfTweets.append({'Tweet Coordinates': unicode(tweet.coordinates)})
        listOfTweets.append({'Retweet Count': unicode(tweet.retweet_count)})
        listOfTweets.append({'Retweed': unicode(tweet.retweeted)})
        listOfTweets.append({'Phone Type': unicode(tweet.source)})
        #listOfTweets.append({'Sensitive': })
        listOfTweets.append({'Language': unicode(tweet.lang)})
    return listOfTweets

def getRetweetAvg(listOfTweets):
    numOfRetweets = 0
    count = 0
    for tweet in listOfTweets:
        if tweet.get('Retweet Count'):
            numOfRetweets += int(tweet.get('Retweet Count'))
        count += 1
    return float(numOfRetweets/count)

def getRetweetTotal(listOfTweets):
    numOfRetweets = 0
    for tweet in listOfTweets:
        if tweet.get('Retweet Count'):
            numOfRetweets += int(tweet.get('Retweet Count'))
    return numOfRetweets
"""
def getRetweetPercent(listOfTweets):
    peopleRetweet = 0
    peopleTotal = 0
    for tweet in listOfTweets:
        if tweet.get('Retweet Count'):
            if int(tweet.get('Retweet Count')) > 0:
                peopleRetweet += int(tweet.get('Retweet Count'))
                peopleTotal += int(tweet.get('Retweet Count'))
            else:
    return numOfRetweets
"""

#listOfTweets = [{}]
#get_tweets(listOfTweets, "ok", 10)
#listOfTweets = get_tweets(listOfTweets, '#PokemonGo', 200)
#print process_tweets(listOfTweets)

#for i in listOfTweets:
#    if i.get('Retweet Count'):
#        print i.get('Retweet Count')

#The dot operator allows for EASY dict-value getting
#process_data(data)
#for tweet in data:
#    print_tweet(tweet)

