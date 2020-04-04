# Import the Twython class
from twython import Twython
import os
from dotenv import load_dotenv
import pandas as pd
import csv

from geopy.geocoders import Nominatim
import gmplot
from twython import TwythonStreamer

# Load credentials from json file
load_dotenv()

# Query 
query='virus'

# Filter out unwanted data
def process_tweet(tweet):
    d = {}
    d['hashtags'] = [hashtag['text'] for hashtag in tweet['entities']['hashtags']]
    d['text'] = tweet['text']
    d['user'] = tweet['user']['screen_name']
    d['user_loc'] = tweet['user']['location']
    return d 

# Create a class that inherits TwythonStreamer
class MyStreamer(TwythonStreamer):     

    # Received data
    def on_success(self, data):

        # Only collect tweets in English
        if data['lang'] == 'en':
            tweet_data = process_tweet(data)
            self.save_to_csv(tweet_data)

    # Problem with the API
    def on_error(self, status_code, data):
        print(status_code, data)
        self.disconnect()

    # Save each tweet to csv file
    def save_to_csv(self, tweet):
        with open(r'saved_tweets.csv', 'a') as file:
            writer = csv.writer(file)
            writer.writerow(list(tweet.values()))

# Instantiate an object
stream = MyStreamer(os.getenv('CONSUMER_KEY'), os.getenv('CONSUMER_SECRET'),os.getenv('ACCESS_TOKEN'),os.getenv('ACCESS_SECRET'))

# Start the stream
stream.statuses.filter(track=query)

tweets = pd.read_csv("saved_tweets.csv")

geolocator = Nominatim()

# Go through all tweets and add locations to 'coordinates' dictionary
coordinates = {'latitude': [], 'longitude': []}
for count, user_loc in enumerate(tweets.location):
    try:
        location = geolocator.geocode(user_loc)
        
        # If coordinates are found for location
        if location:
            coordinates['latitude'].append(location.latitude)
            coordinates['longitude'].append(location.longitude)
            
    # If too many connection requests
    except:
        pass
    
# Instantiate and center a GoogleMapPlotter object to show our map
gmap = gmplot.GoogleMapPlotter(30, 0, 3)

# Insert points on the map passing a list of latitudes and longitudes
gmap.heatmap(coordinates['latitude'], coordinates['longitude'], radius=20)

# Save the map to html file
gmap.draw("python_heatmap.html")

