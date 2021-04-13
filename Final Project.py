from bs4 import BeautifulSoup
import requests
import unittest
import sqlite3
import json
import os

def getLink(soup):
    url = "https://www.zillow.com/washtenaw-county-mi/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22Washtenaw%20County%2C%20MI%22%2C%22mapBounds%22%3A%7B%22west%22%3A-84.2349121040437%2C%22east%22%3A-83.15563025611971%2C%22south%22%3A42.11028501569724%2C%22north%22%3A42.565699612405055%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A2869%2C%22regionType%22%3A4%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%7D"
    links = soup.findAll('div', {'class': 'list-card-price'})
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    homes = soup.findAll('div', {'class': 'list-card-price'})
    forsale = []
    for price in homes[0:10]:
        forsale.append("https://www.zillow.com/" + price['href'])
    return forsale 



def main():
    url = "https://www.zillow.com/washtenaw-county-mi/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22Washtenaw%20County%2C%20MI%22%2C%22mapBounds%22%3A%7B%22west%22%3A-84.2349121040437%2C%22east%22%3A-83.15563025611971%2C%22south%22%3A42.11028501569724%2C%22north%22%3A42.565699612405055%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A2869%2C%22regionType%22%3A4%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%7D"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    getLink(soup)

class TestAllMethods(unittest.TestCase):
    def setUp(self):
        self.soup = BeautifulSoup(requests.get('').text, 'html.parser')


if __name__ == "__main__":
    main()
    unittest.main(verbosity = 2)