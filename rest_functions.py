import tweepy
import json
import time
import datetime
import moment      # Used to parse tweet date
from keys import * 


#Set up Twitter Authentication
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
    aaa = []
    pts = [-1,0,0,0,0,0]
    index = -1
    #timeStamps.append("Time")
    for tweet in listOfTweets:
        #timeStamps.append(tweet['Tweet Created At'])
        timestring = tweet['Tweet Created At']
        #print timestring
        m = moment.date(timestring, '%Y-%m-%d %H:%M:%S')
        print str(m.month) + " " + str(m.day) + " " + str(m.hour) + " " + str(m.minute) + " " + str(m.second)
        ts = [m.year, m.month, m.day, m.hour, m.minute, m.second]
        if pts == ts:
            aaa[index][1] += 1
        else:
            aaa.append([ts, 1])
            index += 1
        if index >= 20:
            break
        pts = ts
    print aaa
    return aaa

def getMiscData(listOfTweets):
    arr = []
    arr.append(getRetweetCount(listOfTweets))
    arr.append(getRetweetAvg(listOfTweets))
    return arr

def getDisplayedTweets(listOfTweets):
    displayedTweets = []
    for tweet in listOfTweets:
        userTweet = []
        userTweet.append(tweet['User Name'])
        userTweet.append(tweet['Tweet Text'])
        displayedTweets.append(userTweet)
    return displayedTweets

def getTweetFreq(listOfTweets):
    if len(listOfTweets) >= 95:
        return "Your keyword is tweeted a lot!"
    return "Your keyword is infrequently used."

listOfTweets = []
#get_tweets(listOfTweets, "ok", 10)
listOfTweets = get_tweets(listOfTweets, 'friends', 2)
getDisplayedTweets(listOfTweets)
print getTweetsOverTime(listOfTweets)
#arr = getTweetsOverTime(listOfTweets)
