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
def get_artist_reviews():
    artist_information = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
    }
    urls = ['https://www.metacritic.com/person/taylor-swift', 'https://www.metacritic.com/person/frank-ocean', 'https://www.metacritic.com/person/dua-lipa', 'https://www.metacritic.com/person/justin-bieber']
    for i in urls:
        r = requests.get(i, headers = headers)
        soup = BeautifulSoup(r.text, 'html.parser')
        average_career_score = soup.find_all('td', class_ = 'summary_score')
        highest_score = soup.find_all('tr', class_='highest_review')
        lowest_score = soup.find_all('tr', class_='lowest_review last')
        newest_release = soup.find_all('td', class_='title brief_metascore')
        print(newest_release)
        artist_information.append((average_career_score, highest_score, lowest_score))
    

def main():
    get_artist_reviews()

class TestAllMethods(unittest.TestCase):
    def setUp(self):
        self.soup = BeautifulSoup(requests.get('').text, 'html.parser')


if __name__ == "__main__":
    main()
    unittest.main(verbosity = 2)