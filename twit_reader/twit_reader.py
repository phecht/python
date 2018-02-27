'''twit_reader reads tweets and puts them in a sqlite3 DB'''
import sqlite3
from twitter_scraper import get_tweets

UNAME = 'YahooNews'

def create_table():
    '''create table twitlite '''
    conn = sqlite3.connect("twitlite.db")
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS twits")
    conn.commit()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS twits(id INTEGER PRIMARY KEY, twituser STRING, twitText TEXT)")
    conn.commit()
    conn.close()

def delete(deleteid):
    '''Delete a record in SQLite3'''
    conn = sqlite3.connect("twitlite.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM twits  WHERE id=?", (deleteid))
    conn.commit()
    conn.close()

def insert(twit_user, tweet_text):
    '''insert a record'''
    conn = sqlite3.connect("twitlite.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO twits VALUES (?,?,?)", (None, twit_user, tweet_text))
    conn.commit()
    conn.close()

def view():
    '''view all records'''
    conn = sqlite3.connect("twitlite.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM twits")
    view_rows = cursor.fetchall()
    conn.close()
    return view_rows

create_table()

TWEET_COUNT = 0
for tweet in get_tweets(UNAME, pages=2):
    print(TWEET_COUNT)
    print(tweet)
    insert(UNAME, tweet)
    TWEET_COUNT = TWEET_COUNT+1


TWEET_ROWS = view()
for row in TWEET_ROWS:
    print(row)
