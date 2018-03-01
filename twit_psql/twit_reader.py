'''twit_reader reads tweets and puts them in a postgreSQL DB using psycopg2'''
import argparse
import psycopg2
from twitter_scraper import get_tweets

PARSER_ARGS = argparse.ArgumentParser()
PARSER_ARGS.add_argument('-p', '--password', required=True)
PARSER_ARGS.add_argument('-u', '--user', required=True)

ALL_ARGS = PARSER_ARGS.parse_args()

print(ALL_ARGS.password)
PASSWORD_DB = ALL_ARGS.password
UNAME = ALL_ARGS.user

CONN_STRING = "dbname='database1' user='phecht' password=" + "'" + PASSWORD_DB + "'" \
    + ' host=localhost'

def create_table():
    '''create table twits '''
    print(CONN_STRING)
    conn = psycopg2.connect(CONN_STRING)
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS twits")
    conn.commit()
    cursor.execute("CREATE TABLE IF NOT EXISTS twits(id SERIAL primary key, twituser TEXT, twitText TEXT);")
    conn.commit()
    conn.close()

def delete(deleteid):
    '''Delete a record in psycopg2'''
    conn = psycopg2.connect(CONN_STRING)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM twits  WHERE id=?", (deleteid))
    conn.commit()
    conn.close()

def insert(twit_user, tweet_text):
    '''insert a record'''
    conn = psycopg2.connect(CONN_STRING)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO twits (twituser, twitText) VALUES (%s,%s)", (twit_user, tweet_text))
    conn.commit()
    conn.close()

def view():
    '''view all records'''
    conn = psycopg2.connect(CONN_STRING)
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
