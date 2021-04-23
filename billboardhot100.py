import os
import sqlite3
import unittest
import billboard

def getChart(date):
    # starter code to pull from Billboard API from: https://rapidapi.com/LDVIN/api/billboard-api
    data = billboard.ChartData('hot-100', date = date)
    return data

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
    curr.execute("CREATE TABLE %s (Rank INTEGER, Title TEXT, Artist TEXT)" % tablename)
    conn.commit()

def insert_data(data, tablename, curr, conn, chunksize = 25):
    """
    * Insert chart data in chunks of 25.
    """
    for index in range(0, len(data.entries), chunksize):
        values = []
        entries = data.entries[index:index+chunksize]
        for rank, entry in enumerate(entries):
            values.append('(%s,"%s","%s")' % (rank + 1 + index, entry.title, entry.artist))
        curr.execute("INSERT INTO %s (Rank,Title,Artist) VALUES %s" % (tablename, ','.join(values)))
        conn.commit()
    
    
def main():
    """
    * Perform key steps in order.
    """
    dt = "2021-04-20"
    db_name = "Chart_Data_%s.db" % dt.replace('-', '_')
    tablename = 'Billboard_Hot_100' 
    data = getChart(dt)
    curr, conn = setUpDatabase(db_name)
    setUpHot100Table(tablename,curr,conn)
    insert_data(data,tablename,curr,conn)

if __name__ == "__main__":
    main()
    unittest.main(verbosity = 2)