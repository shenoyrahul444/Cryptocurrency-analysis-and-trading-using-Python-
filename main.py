# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 22:03:47 2018

@author: Rahul Shenoy
"""

"""
Previous commands:::
    pip install tweepy
    pip install textblob
    python -m textblob.download_corpora             #Corpora is a larget and structured set of texts
"""

import re        #Regular Expression: For data cleaning
import tweepy    #Python client for Twitter API
import textblob  #For Processing textual data
from tweepy import OAuthHandler
from textblob import TextBlob

class TwitterClient(object):    
    #Twitter Class for sentiment Analysis
    def __init__(self):     #Constructor
        consumer_key = "KnAtSkrhoVM783xSuHSWtpng2"
        consumer_secret = "OQTS2CSXio6jTAsTCAeh9NCdDk1Vp0vzhnnkVe2SkP9GjkF5xm"
        access_token = "2445815269-OsDebyuWMjhiiLl622n07RalRbNpRuAMiZxRRsN"
        access_token_secret = "pA0rt3QfXACOjXBDrfv1qzd7w8i3MWZSrRDD9gTs8eQPn"
        
        #Attempt Authentication
        try:
            #Creating OAuth Handler Object
            self.auth = OAuthHandler(consumer_key,consumer_secret)
            self.auth.set_access_token(access_token,access_token_secret)
            self.api = tweepy.API(self.auth)
        except:
            print("Error : Authentication Failed")

#    def clean_tweet(self,tweet):
#            """This will clean the tweet            """
#                 return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

    def get_tweet_sentiment(self,tweet):
        """Uses TextBlobs Sendtiment Analysis method to find sentiment of the tweet
        TextBlob uses a Movies Reviews dataset in which reviews have already been labelled as positive or negative.
        Positive and negative features are extracted from each positive and negative review respectively.
        Training data now consists of labelled positive and negative features. This data is trained on a Naive Bayes Classifier.
        """
    def get_tweets(self,query,count=10):
        tweets = []
        
        try:
            fetched_tweets = self.api.search(q=query,count = count)
#            print(fetched_tweets)
            return fetched_tweets
#            for tweet in fetched_tweets:
#                parsed_tweet = {}
#                parsed_tweet['text'] = tweet.text
#                parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text)
#                
#                if tweet.retweet_count > 0:
#                    if parsed_tweet not in tweets:
#                        tweets.append(parsed_tweet)
#                else:
#                    tweets.append(parsed_tweet)
#            return tweets
        except tweepy.TweepError as e:
            print("Error: %s" % str(e))
            
def main():
    api = TwitterClient()       #Creating TwitterClient Object
#    public_tweets = api.api.home_timeline()
#    for tweet in public_tweets:
#        print(tweet.text,"\n")
    tweets = api.get_tweets(query ="litecoin",count = 100)
    for tweet in tweets:
        print(tweet.text,"\n")

if __name__ == "__main__":
    main()
    
    