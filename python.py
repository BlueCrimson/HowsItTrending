#TODO MOTION TOWARDS PYTHON 3
from flask import Flask, render_template
from flask import request
from rest_functions import *
import tweepy
import time
import json
#from keys import classes/functions and etc


app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")
#RESULTS PAGE
@app.route('/results', methods=['POST'])
def my_form_post():
    listOfTweets = []   #A list of tweets(dictionary)
    numOfTweets = 100
    #text = request.form #returns the array
    keyword = request.form["search_query"]  #Grab input data from the form
    try:
        tweet_list = get_tweets(listOfTweets, keyword, numOfTweets)
        retweetAvg = getRetweetAvg(tweet_list)  #Returns average # of retweets per post
        retweetPercent = getRetweetPercent(tweet_list)  #Returns the % of posts were a retweet
        retweetCount = getRetweetCount(tweet_list)      #Returns the total retweet count
        devicePercent = getPhoneTypePercent(tweet_list)
        devicePercent = json.dumps(devicePercent, ensure_ascii=False) #converts to JSON OBJ, ensure_ascii=False means it will be treated as unicode
        tweetsOverTime = getTweetsOverTime(tweet_list)  #Returns list ofDictionary of (time, tweet_text)
        miscData = getMiscData(tweet_list)      #Returns some raw stats for display
        return render_template("results.html", dog = tweet_list, retweetAvg = retweetAvg, retweetPercent = retweetPercent, devicePercent = devicePercent, tweetsOverTime = tweetsOverTime, miscData = miscData)
    except:
        return render_template("bad_results.html")
if __name__ == "__main__":
    app.run()
