# Import the Twython class
from twython import Twython
import os
from dotenv import load_dotenv
import pandas as pd

# Load credentials from json file
load_dotenv()

# Instantiate an object
python_tweets = Twython(os.getenv('CONSUMER_KEY'), os.getenv('CONSUMER_SECRET'))

# Create our query
query = {'q': 'covid-1',
        'result_type': 'popular',
        'count': 10,
        'lang': 'en',
        }
        
# Search tweets
dict_ = {'user': [], 'date': [], 'text': [], 'favorite_count': []}
for status in python_tweets.search(**query)['statuses']:
    dict_['user'].append(status['user']['screen_name'])
    dict_['date'].append(status['created_at'])
    dict_['text'].append(status['text'])
    dict_['favorite_count'].append(status['favorite_count'])

# Structure data in a pandas DataFrame for easier manipulation
df = pd.DataFrame(dict_)
df.sort_values(by='favorite_count', inplace=True, ascending=False)
print(df.head(5))