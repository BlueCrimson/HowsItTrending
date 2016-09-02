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
        dict_ = {'Screen Name': tweet.user.screen_name,
            'User Name': tweet.user.name,
            'Tweet Created At': unicode(tweet.created_at),
            'Tweet Text': tweet.text,
            'User Location': unicode(tweet.user.location),
            'Tweet Coordinates': unicode(tweet.coordinates),
            'Retweet Count': unicode(tweet.retweet_count),
            'Retweeted': unicode(tweet.retweeted),
            'Phone Type': unicode(tweet.source)
                }
        listOfTweets.append(dict_)   
    return listOfTweets

def getRetweetAvg(listOfTweets):
    numOfRetweets = 0
    count = 0
    for tweet in listOfTweets:
        if tweet.get('Retweet Count'):
            numOfRetweets += int(tweet.get('Retweet Count'))
        count += 1
    if count == 0:
        return 0
    else:
        return float(numOfRetweets/count)

def getRetweetCount(listOfTweets):
    numOfRetweets = 0
    for tweet in listOfTweets:
        if tweet.get('Retweet Count'):
            numOfRetweets += int(tweet.get('Retweet Count'))
    return numOfRetweets

def getRetweetPercent(listOfTweets):
    peopleTotal = len(listOfTweets)
    peopleRetweet = 0
    for tweet in listOfTweets:
        if tweet.get('Retweeted'):
            if (tweet.get('Retweeted') == "True"):
                peopleRetweet += 1
    return float(peopleRetweet/peopleTotal)

def phoneTypePercent(listOfTweets):
    peopleTotal = len(listOfTweets)
    phoneTypes = {}
    #print listOfTweets[2]
    for tweet in listOfTweets:
        print tweet['Phone Type']

    #return #phoneTypes



listOfTweets = []
#get_tweets(listOfTweets, "ok", 10)
listOfTweets = get_tweets(listOfTweets, '#PokemonGo', 2)
phoneTypePercent(listOfTweets)

#for i in listOfTweets:
#    if i.get('Retweet Count'):
#        print i.get('Retweet Count')

#The dot operator allows for EASY dict-value getting
#process_data(data)
#for tweet in data:
#    print_tweet(tweet)
