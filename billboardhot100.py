import os
import sqlite3
import unittest
import billboard
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def getChart(date):
    """
    Accessing Hot 100 Songs
    """
    # starter code to pull from Billboard API from: https://rapidapi.com/LDVIN/api/billboard-api
    data = billboard.ChartData('hot-100', date = date)
    return data

def getArtistChart(date):
    """
    Accessing Artist 100
    """
    data1 = billboard.ChartData('artist-100', date = date)
    return data1

# Create Database
def setUpDatabase(db_name):
    """
    * Create database to store data.
    """
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db_name)
    curr = conn.cursor()
    return curr, conn

def setUpHot100Table(tablename, curr, conn):
    """
    * Create table containing Top 100 Billboard songs.
    """
    curr.execute("DROP TABLE IF EXISTS %s" % tablename)
    curr.execute("CREATE TABLE %s (Rank INTEGER, Title TEXT, Artist TEXT, Weeks INTEGER)" % tablename)
    conn.commit()

def setUpHArtist100Table(tablename_artist, curr, conn):
    """
    * Create table containing Top 100 Billboard Artists.
    """
    curr.execute("DROP TABLE IF EXISTS %s" % tablename_artist)
    curr.execute("CREATE TABLE %s (Rank INTEGER, Artist TEXT, Weeks INTEGER)" % tablename_artist)
    conn.commit()

def insert_data(data, tablename, curr, conn, chunksize = 25):
    """
    * Insert chart data in chunks of 25. Hot 100
    """
    for index in range(0, len(data.entries), chunksize):
        values = []
        entries = data.entries[index:index+chunksize]
        for rank, entry in enumerate(entries):
            values.append('(%s,"%s","%s","%s")' % (rank + 1 + index, entry.title, entry.artist, entry.weeks))
        #curr.execute("DROP TABLE IF EXISTS %s)" % tablename)
        curr.execute("INSERT INTO %s (Rank,Title,Artist,Weeks) VALUES %s" % (tablename, ','.join(values)))
        conn.commit()

def insert_artist_data(data1, tablename_artist, curr, conn, chunksize = 25):
    """
    * Insert artist 100 data in chunks of 25. Artist 100
    """
    for index in range(0, len(data1.entries), chunksize):
        values = []
        entries = data1.entries[index:index+chunksize]
        for rank, entry in enumerate(entries):
            values.append('(%s,"%s","%s")' % (rank + 1 + index, entry.artist, entry.weeks))
        #curr.execute("DROP TABLE IF EXISTS %s)" % tablename_artist)
        curr.execute("INSERT INTO %s (Rank,Artist,Weeks) VALUES %s" % (tablename_artist, ','.join(values)))
        conn.commit()

def insert_mytop100(artistFrequency):
    """
    Christina's Top 100 Songs
    """
    path = os.path.dirname(os.path.abspath(__file__))
    chartConnPath = path+'/Chart_Data_2021_04_20.db'
    chartConn = sqlite3.connect(chartConnPath)
    chartCursor = chartConn.cursor()
    topArtists = pd.read_csv('my-top-100.csv', encoding = "UTF-8", index_col = [0])
    topArtists.columns = topArtists.columns.str.strip()
    topArtists.columns = topArtists.columns.str.replace("."," ")
    topArtists.to_sql(artistFrequency, chartConn, if_exists='replace')
    chartConn.commit()

def insert_addie(songTable):
    """
    Addie's Top 100 Songs
    """
    path = os.path.dirname(os.path.abspath(__file__))
    chartConnPath = path+'/Chart_Data_2021_04_20.db'
    chartConn = sqlite3.connect(chartConnPath)
    chartCursor = chartConn.cursor()
    topSongs = pd.read_csv('addie-top-100.csv', encoding = "UTF-8", index_col = [0])
    topSongs.columns = topSongs.columns.str.strip()
    topSongs.columns = topSongs.columns.str.replace("."," ")
    topSongs.to_sql(songTable, chartConn, if_exists='replace')
    chartConn.commit()

def get_conns():
    path = os.path.dirname(os.path.abspath(__file__))
    chartConnPath = path+'/Chart_Data_2021_04_20.db'
    chartConn = sqlite3.connect(chartConnPath)
    chartCursor = chartConn.cursor()
    return chartConn, chartCursor

def count_frequencies(chartConn, chartCursor, songTable, frequencyTable):
    """
    * Count number of times top song favorites appear on
    billboard.
    """
    columns = ["Artist", "Title", "Present"]
    values = list(chartCursor.execute("SELECT A.Artist, A.Title, B.popularity FROM Billboard_Hot_100 AS A LEFT OUTER JOIN %s AS B ON A.Title = B.name AND A.Artist = B.artist;" % songTable))
    chartCursor.execute("DELETE FROM %s WHERE True" % frequencyTable)
    data = pd.DataFrame(values).rename(columns = { num : columns[num] for num in range(len(columns))})
    data["Present"] = data["Present"].apply(lambda x : 0 if pd.isnull(x) else 1)
    data.to_sql(frequencyTable, chartConn, if_exists='replace')

def count_frequencies2(chartConn, chartCursor, artistFrequency, artistTable):
    """
    * Count number of times top artists favorites appear on
    billboard.
    """
    columns = ["Artist", "Present"]
    values = list(chartCursor.execute("SELECT DISTINCT A.Artist, B.popularity FROM Billboard_Artist_100 AS A LEFT OUTER JOIN %s AS B ON A.Artist = B.artist;" % artistFrequency))
    chartCursor.execute("DELETE FROM %s WHERE True" % artistTable)
    data = pd.DataFrame(values).rename(columns = { num : columns[num] for num in range(len(columns))})
    data["Present"] = data["Present"].apply(lambda x : 0 if pd.isnull(x) else 1)
    data = data.drop_duplicates(subset = ["Artist"])
    data.to_sql(artistTable, chartConn, if_exists='replace')

def get_results(chartCursor, frequencyTable, artistTable):
    """
    Write a text file concluding all results from both tables (hot 100 and artist 100)
    """
    values = chartCursor.execute("SELECT sum(Present)*1.0 / count(Present) FROM %s" % frequencyTable)
    values = values.fetchone()
    values2 = chartCursor.execute("SELECT sum(Present)*1.0 / count(Present) FROM %s" % artistTable)
    values2 = values2.fetchone()
    file = open("myavg_dance.txt","a")
    file.write(" Addie listens to " + str((values[0]*100)) + " percent of songs from the Billboard Hot 100. "
    
    "Christina listens to " + str((values[0]*100)) + " percent of artists from the Billboard Artist 100. ")
    file.close()

def main():
    """
    * Perform key steps in order.
    """
    dt = "2021-04-20"
    db_name = "Chart_Data_%s.db" % dt.replace('-', '_')
    tablename = 'Billboard_Hot_100' 
    tablename_artist = 'Billboard_Artist_100'
    data = getChart(dt)
    data1 = getArtistChart(dt)
    curr, conn = setUpDatabase(db_name)
    setUpHot100Table(tablename,curr,conn)
    setUpHArtist100Table(tablename_artist,curr,conn)
    curr.execute("DELETE FROM %s WHERE True" % tablename)
    insert_data(data,tablename,curr,conn)
    curr.execute("DELETE FROM %s WHERE True" % tablename_artist)
    insert_artist_data(data1,tablename_artist,curr,conn)

def main_2():
    songTable = "MyTopSongs_Addie"
    frequencyTable = "Addie_Billboard"
    artistFrequency = "Christina_TopArtists" 
    artistTable = "Christina_Billboard"
    insert_addie(songTable)
    insert_mytop100(artistFrequency)
    chartConn, chartCursor = get_conns()
    count_frequencies(chartConn, chartCursor, songTable, frequencyTable)
    count_frequencies2(chartConn, chartCursor, artistFrequency, artistTable)
    print(get_results(chartCursor, frequencyTable, artistTable))

if __name__ == "__main__":
    main()
    main_2()
    unittest.main(verbosity = 2)
