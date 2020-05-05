# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 23:55:10 2020

@author: Songlap
"""

import GetOldTweets3 as got
import pandas as pd

text_query = 'Monzo'
since_date = '2020-02-01'
until_date = '2020-04-29'
count = 5000
# Creation of query object
tweetCriteria = got.manager.TweetCriteria().setQuerySearch(text_query).setSince(since_date).setUntil(until_date).setMaxTweets(count)
# Creation of list that contains all tweets
tweets = got.manager.TweetManager.getTweets(tweetCriteria)
# Creating list of chosen tweet data
text_tweets = [[tweet.date, tweet.text] for tweet in tweets]

text_tweets_df=pd.DataFrame(text_tweets)
text_tweets_df.to_csv("D:\Kasturi\Python\Twitter\Monzo.csv")