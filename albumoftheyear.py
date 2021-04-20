from bs4 import BeautifulSoup
import requests
import os
import csv
import sqlite3
import unittest

# Create Database
def setUpDatabase(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    return cur, conn

# Get Dua Lipa's, Taylor Swift's, Frank Ocean's, and Justin Bieber's critic score and user score & their album reviews
def get_artist_reviews(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
    }
    r = requests.get(url, headers = headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    average_career_score = soup.find('td', class_ = 'summary_score').find('span').text
    highest_score = soup.find('tr', class_='highest_review').find_all('span')
    highest_score = ' '.join([item.text.strip() for item in highest_score])
    lowest_score = soup.find('tr', class_='lowest_review last').find_all('span')
    lowest_score = ' '.join([item.text.strip() for item in lowest_score])

    releases = soup.find_all('td', class_='title brief_metascore')
    releases = [item.find('span').text + ' ' + item.find('a').text for item in releases]

    return [average_career_score, highest_score, lowest_score, releases]

    

def main():
    url = 'https://www.metacritic.com/person/'
    artists = ['taylor-swift', 'frank-ocean', 'dua-lipa', 'justin-bieber'] #put artists in text file read them in from text file
    for artist in artists:
        get_artist_reviews(url + artist) #save result to db

class TestAllMethods(unittest.TestCase):
    def setUp(self):
        self.soup = BeautifulSoup(requests.get('').text, 'html.parser')


if __name__ == "__main__":
    main()
    unittest.main(verbosity = 2)