from bs4 import BeautifulSoup
from urllib.request import urlopen
import unittest
import sqlite3
import pandas as pd
import json
import os

#from requests.models import get_auth_from_url

# Create Database
def setUpDatabase(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    return cur, conn


''' Get Justin Bieber's and Taylor Swift's tweets in the last month (or last 100 tweets) and put it into a dictionary, gather each tweets retweets 
    example of dictionary output {Justin Bieber: {tweet: x retweets, tweet: retweets, etc.}, Taylor Swift: {tweet: retweets, tweet: retweets, etc.}} 
    Sort in descending order of how many retweets'''

def getLink(handle):
    url = 'https://twitter.com/'+ handle
    html = urlopen(url)
    soup = BeautifulSoup(html, 'html.parser')
    # Gets the tweet
    find_tweets = soup.findAll('span', {'class': "css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0"})
    find_retweets = soup.find('span', {'class': 'css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0'})
    find_tweet = soup.findAll('div', {'class': 'css-1dbjc4n r-18u37iz'})
    breakpoint()
    #data-testid="tweet">
    #find_tweets = soup.find_all("li", attrs={"class":"js-stream-item"})
    # if find_tweets:
    #     for tweet in find_tweets:
    #         #retweets
    #        soup.find('span', {'class': 'css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0'})
    # else: 
    #     print("Account username not found.")







def main():
    handle = 'justinbieber'
    getLink(handle)

class TestAllMethods(unittest.TestCase):
    def setUp(self):
        self.soup = BeautifulSoup(requests.get('').text, 'html.parser')


if __name__ == "__main__":
    main()
    unittest.main(verbosity = 2)