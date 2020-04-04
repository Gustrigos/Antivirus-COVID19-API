# Import the Twython class
from twython import Twython
import os
from dotenv import load_dotenv
import pandas as pd
import datetime as dt

# Load credentials from json file
load_dotenv()

# Instantiate an object
python_tweets = Twython(os.getenv('CONSUMER_KEY'), os.getenv('CONSUMER_SECRET'))

twitter_accounts = pd.read_csv("cuentas_twitter.csv")
twitter_accounts.dropna(axis=0,how='any',inplace=True)
twitter_accounts.set_index('cuenta',inplace=True)

# Create our query
users = twitter_accounts.index.values

# Number of posts to download (max 200 per request)
tweet_num = 15    
retweets = 0

# Search tweets
dict_ = {'user': [], 'date': [], 'text': [], 'favorite_count': [], 'entity': [], 'category': []}

df = pd.DataFrame()

for user in users:
	for status in python_tweets.get_user_timeline(screen_name=user,count=tweet_num,include_rts=retweets,):
	    dict_['user'].append(status['user']['screen_name'])
	    dict_['date'].append(status['created_at'])
	    dict_['text'].append(status['text'])
	    dict_['favorite_count'].append(status['favorite_count'])
	    dict_['entity'].append(twitter_accounts.loc[user,'entidad'])
	    dict_['category'].append(twitter_accounts.loc[user,'categoria'])
	    df_temp = pd.DataFrame(dict_)
	    df_temp.set_index('user',inplace=True)
	    df = pd.concat([df,df_temp])


# Structure data in a pandas DataFrame for easier manipulation
#df = pd.DataFrame(dict_)
#df.sort_values(by='date', inplace=True, ascending=True)
print(df.head(5))
df.to_csv("tweets_log/tweets_{}.csv".format(dt.date.today()))
