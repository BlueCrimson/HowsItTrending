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
        listOfTweets.append({'Tweet Created At': str(tweet.created_at)})
        listOfTweets.append({'Tweet Text': tweet.text})
        listOfTweets.append({'User Location': str(tweet.user.location)})
        listOfTweets.append({'Tweet Coordinates': str(tweet.coordinates)})
        listOfTweets.append({'Retweet Count': str(tweet.retweet_count)})
        listOfTweets.append({'Retweed': str(tweet.retweeted)})
        listOfTweets.append({'Phone Type': str(tweet.source)})
        #listOfTweets.append({'Sensitive': })
        listOfTweets.append({'Language': str(tweet.lang)})
    return listOfTweets

def process_tweets(listOfTweets):
    numOfRetweets = 0
    count = 0
    for tweet in listOfTweets:
        if tweet.get('Retweet Count'):
            numOfRetweets += int(tweet.get('Retweet Count'))
        count += 1
    test = numOfRetweets/count
    return float(numOfRetweets/count)



#listOfTweets = [{}]
#print get_tweets(listOfTweets, "ok", 1)
#listOfTweets = get_tweets(listOfTweets, '#PokemonGo', 1)
#print process_tweets(listOfTweets)

#for i in listOfTweets:
#    if i.get('Retweet Count'):
#        print i.get('Retweet Count')

#The dot operator allows for EASY dict-value getting
#process_data(data)
#for tweet in data:
#    print_tweet(tweet)

