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
from keys import Keys


class TwitterClient(object):    
    #Twitter Class for sentiment Analysis
    def __init__(self):     #Constructor
        
        keys = Keys()
        [consumer_key,consumer_secret,access_token,access_token_secret] = keys.get_keys()

        try:
            #Creating OAuth Handler Object
            self.auth = OAuthHandler(consumer_key,consumer_secret)
            self.auth.set_access_token(access_token,access_token_secret)
            self.api = tweepy.API(self.auth)
        except:
            print("Error : Authentication Failed")

    def clean_tweet(self,tweet):
        """For cleaning the tweets"""
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

    def get_tweet_sentiment(self,tweet):
        """Uses TextBlobs Sendtiment Analysis method to find sentiment of the tweet
        TextBlob uses a Movies Reviews dataset in which reviews have already been labelled as positive or negative.
        Positive and negative features are extracted from each positive and negative review respectively.
        Training data now consists of labelled positive and negative features. This data is trained on a Naive Bayes Classifier.
        """
        analysis = TextBlob(self.clean_tweet(tweet))
#        print(analysis)
        
        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'
            
    def get_tweets(self,query,count=10):
        
        tweets = []
        
        try:
            fetched_tweets = self.api.search(q=query,count = count)
#            print(fetched_tweets)
#            return fetched_tweets
            for tweet in fetched_tweets:
                parsed_tweet = {}
                parsed_tweet['text'] = tweet.text
                parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text)
                
                if tweet.retweet_count > 0:
                    if parsed_tweet not in tweets:
                        tweets.append(parsed_tweet)
                else:
                    tweets.append(parsed_tweet)
            return tweets
        except tweepy.TweepError as e:
            print("Error: %s" % str(e))
            
def main():
    api = TwitterClient()       #Creating TwitterClient Object
#    public_tweets = api.api.home_timeline()
#    for tweet in public_tweets:
#        print(tweet.text,"\n")
    tweets = api.get_tweets(query ="litecoin",count = 100)
    
    ptweets = []
    ntweets = []
    
    for tweet in tweets:
        if tweet['sentiment'] == 'positive':
            ptweets.append(tweet)
        elif tweet['sentiment'] == 'negative':
            ntweets.append(tweet)
#    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
    print('Positive tweets percentage : %s ' % str((len(ptweets)*100)/len(tweets)))
    
#    ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
    print('Negative tweets percentage : %s ' % ((len(ntweets)*100)/len(tweets)))
    
    print("***************************** Positive Tweets **********************************\n")
    for tweet in ptweets:
        print(tweet['text'],"\n")
        
    print('\n\n\n\n')
    
    print("***************************** Negative Tweets **********************************\n")
    for tweet in ntweets:
        print(tweet['text'],"\n")
    
    
if __name__ == "__main__":
    main()
    
    
