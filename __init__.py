import psycopg2 as sql
con = sql.connect(host="localhost", dbname='ishaan', user='postgres', password="123") 
cur = con.cursor()

"""created a connection betweeen python and postgres and named it con 
in con created a cursor named cur"""
try:
    # cur.execute("DROP TABLE ishaan_table")
    cur.execute("CREATE TABLE ishaan_table(name varchar(30) NOT NULL primary key, date  date )")
    con.commit()
    # cur.execute("SELECT * FROM pg_catalog.pg_tables;")
    """created new table named ishaan _table in database ishaan
    and changes are comitted in connection"""

except Exception as e:
    con.rollback()
    print(e)