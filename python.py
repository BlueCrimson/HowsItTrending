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
    listOfTweets = [{}]
    numOfTweets = 100
    #text = request.form #returns the array
    keyword = request.form["search_query"]  #Grab input data from the form
    try:
        tweet_list = get_tweets(listOfTweets, keyword, numOfTweets)
        retweetAvg = getRetweetsAvg(tweet_list)
        return render_template("results.html", dog = tweet_list, work = retweetAvg)
    except:
        return render_template("bad_results.html")
if __name__ == "__main__":
    app.run()
