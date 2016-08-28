from flask import Flask, render_template
from flask import request
from rest_functions import *
import tweepy
import time
import json
#from keys import classes/functions and etc
from keys import *


app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

#RESULTS PAGE
@app.route('/results', methods=['POST'])
def my_form_post():
    tmp_data = []
    text = request.form
    keyword = request.form["text"]  #Grab input data from the form
    for tweet in tweepy.Cursor(api.search, q=keyword).items(1):
        tmp_data.append(tweet)
    lastest_tweet = len(tmp_data) - 1
    tweet_info = print_tweet(tmp_data[lastest_tweet])
    return render_template("results.html", dog = tweet_info)

if __name__ == "__main__":
    app.run()
