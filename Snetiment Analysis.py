#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install pandas')
get_ipython().system('pip install tweepy')
get_ipython().system('pip install vaderSentiment')


# In[2]:


import tweepy
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer


# In[5]:


consumer_key = 'RYBfxBjQaOrT7FpoB9dC8yMi1'
consumer_secret = 'wGJ1UecrtH3kdCmQCqb3w6I6BONV5DcHwwnpiqxZ5dMOqsFZU4'
access_token = 'sn27qMXRwAzEOqKCeKWYgk6ITFYWRwZcuKUlukbQ'
access_token_secret = 'obC6Z0iIedaraJHTwW6QsNzqHjlQUbGciup4ZwrPFXDxQ'


# In[4]:


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

tweets = api.search('Artificial Intelligence', count=200)


data = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['Tweets'])

display(data.head(10))


print(tweets[0].created_at)


# In[6]:


consumer_key = 'RYBfxBjQaOrT7FpoB9dC8yMi1'
consumer_secret = 'wGJ1UecrtH3kdCmQCqb3w6I6BONV5DcHwwnpiqxZ5dMOqsFZU4'
access_token = '967894777-sn27qMXRwAzEOqKCeKWYgk6ITFYWRwZcuKUlukbQ'
access_token_secret = 'obC6Z0iIedaraJHTwW6QsNzqHjlQUbGciup4ZwrPFXDxQ'


# In[7]:


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

tweets = api.search('Artificial Intelligence', count=200)


data = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['Tweets'])

display(data.head(10))


print(tweets[0].created_at)


# In[8]:


consumer_key = 'RYBfxBjQaOrT7FpoB9dC8yMi1'
consumer_secret = 'wGJ1UecrtH3kdCmQCqb3w6I6BONV5DcHwwnpiqxZ5dMOqsFZU4'
access_token = '967894777-sn27qMXRwAzEOqKCeKWYgk6ITFYWRwZcuKUlukbQ'
access_token_secret = 'obC6Z0iIedaraJHTwW6QsNzqHjlQUbGciup4ZwrPFXDxQ'


# In[9]:


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

tweets = api.search('Artificial Intelligence', count=200)


data = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['Tweets'])

display(data.head(10))


print(tweets[0].created_at)


# In[11]:


import nltk
nltk.download('vader_lexicon')


# In[12]:


sid = SentimentIntensityAnalyzer()


listy = []

for index, row in data.iterrows():
  ss = sid.polarity_scores(row["Tweets"])
  listy.append(ss)
  
se = pd.Series(listy)
data['polarity'] = se.values

display(data.head(100))


# In[ ]:




