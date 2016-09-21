import tweepy
import time
import json
import datetime     
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

#STATUS: STABLE
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

#STATUS: STABLE
def getRetweetCount(listOfTweets):
    numOfRetweets = 0
    for tweet in listOfTweets:
        if tweet.get('Retweet Count'):
            numOfRetweets += int(tweet.get('Retweet Count'))
    return numOfRetweets

#STATUS: NAIVE
def getRetweetPercent(listOfTweets):
    peopleTotal = len(listOfTweets)
    peopleRetweet = 0
    for tweet in listOfTweets:
        if tweet.get('Retweeted'):
            if (tweet.get('Retweeted') == "True"):
                peopleRetweet += 1
    return float(peopleRetweet/peopleTotal)

#STATUS: STABLE
def getPhoneTypePercent(listOfTweets):
    peopleTotal = len(listOfTweets)
    phoneTypes = {}
    #print len(phoneTypes)
    match = False   #If phone type has been added to the list yet
    
    for tweet in listOfTweets:
        if len(phoneTypes) == 0:
            phoneTypes.update({ unicode(tweet['Phone Type']): 1 })
        else:
            match = False
            for key, value in phoneTypes.iteritems():
                if key == unicode(tweet['Phone Type']):
                    phoneTypes[unicode(tweet['Phone Type'])] += 1
                    match = True
                    break
            if match == False:
                phoneTypes.update({tweet['Phone Type']: 1})
    return phoneTypes       

def getTweetsOverTime(listOfTweets):
    timeStamps = []
    timeStamps.append({"Time" : "Tweets"})
    for tweet in listOfTweets:
        timeStamps.append({tweet['Tweet Created At'] : tweet['Tweet Text']})
    return timeStamps
"""
def getTweetsOverTime(listOfTweets):
    timeStamps = []
    timeStamps.append(["Time", "Tweets"])
    for tweet in listOfTweets:
        imeStamps.append([tweet['Tweet Created At']], [tweet['Tweet Text']])
    return timeStamps
"""

def getMiscData(listOfTweets):
    arr = []
    arr.append(getRetweetCount(listOfTweets))
    arr.append(getRetweetAvg(listOfTweets))
    return arr

listOfTweets = []
#get_tweets(listOfTweets, "ok", 10)
listOfTweets = get_tweets(listOfTweets, 'friends', 100)
arr = getTweetsOverTime(listOfTweets)
for i in arr:
    for key, value in i.iteritems():
        print key, value


#TODO 9-3-16: CURRENTLY OF LIST OF DICT FOR TWEETS OVER TIME, IMPLMENT GOOGLE CHARTS WITH IT. ALSO, HOW TO COMBINE THE CHARTS APIS TO ONE JS AND MAKE IT A STATIC JS?O

#for i in listOfTweets:
#    if i.get('Retweet Count'):
#        print i.get('Retweet Count')

#The dot operator allows for EASY dict-value getting
#process_data(data)
#for tweet in data:
#    print_tweet(tweet)
