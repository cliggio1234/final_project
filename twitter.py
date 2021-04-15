from bs4 import BeautifulSoup
import requests
import unittest
import sqlite3
import json
import os

''' Get Justin Bieber's and Taylor Swift's tweets in the last month and put it into a dictionary, gather each tweets retweets 
    example of dictionary output {Justin Bieber: {tweet: x retweets, tweet: retweets, etc.}, Taylor Swift: {tweet: retweets, tweet: retweets, etc.}} '''


def getLink(soup):
    handle = 
    r = requests.get('https://twitter.com/'+ handle)
    soup = BeautifulSoup(r.text, 'html.parser')
    all_tweets = {}
    find_tweets = soup.find_all('li','js-stream-item')
    if find_tweets:
        for tweet in find_tweets:
           soup.find('div', {'class' : 'css-1dbjc4n r-18u37iz r-1wtj0ep r-1s2bzr4 r-1mdbhws'}) 
    else: 
        print("Account name not found.")







def main():
    url = 'http://www.twitter.com/'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    getLink(soup)

class TestAllMethods(unittest.TestCase):
    def setUp(self):
        self.soup = BeautifulSoup(requests.get('').text, 'html.parser')


if __name__ == "__main__":
    main()
    unittest.main(verbosity = 2)