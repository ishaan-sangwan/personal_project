import psycopg2 as sql
import os
import sys
import json as js
con = sql.connect(host="localhost", dbname='ishaan', user='postgres', password="123") 
cur = con.cursor()

"""created a connection betweeen python and postgres and named it con 
in con created a cursor named cur"""
try:
    # cur.execute("DROP TABLE ishaan_table")
    # cur.execute("CREATE TABLE ishaan_table(name varchar(30) NOT NULL primary key, date  date )")
    con.commit()

    cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';")
    out = cur.fetchall()
    for i in out:
        print(i)
    """ cur.fetchall fetches all the output from postgresql and dumps it into out
    then out is iterated line by line"""

except Exception as e:
    con.rollback()
    print(e)