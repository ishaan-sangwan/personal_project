import psycopg2 as sql
import os
import sys
import json as js
con = sql.connect(host="localhost", dbname='ishaan', user='postgres', password="123") 
cur = con.cursor()

"""created a connection betweeen python and postgres and named it con 
in con created a cursor named cur"""
def json_column_name(json_file):
    f = open(json_file)
    data = js.load(f)
    column_name = data[0].keys()
    f.close()
    return column_name
    """a json file is opened with alias f
    data is dumped in data list
    an empty list named column_name is made and  
    data is iterated through and all the keys are appended in column_name"""
def json_column_types(json_file):
    f = open(json_file)
    data = js.load(f)
    column_type = []
    for i in data:
        for j in i:
            if data[j] not in column_name:
                column_type.append(data[j])
    return column_type
    """json file is opened and data is loaded into empty list data
    data is iterated over and data[j]'s type is appended to column_type """
    return column_type
json_column_name("distros.json")
 

def creating_table(config_file):
    f1 = open(config_file)
    config = js.load(config_file)
    cur.execute("CREATE TABLE test('s_no numeric primary key')")
    for i in data:
        cur.execute("ALTER TABLE test ADD COLUMN {} {}".format(i, data[i]))
        con.commit()
    f.close()
""" new function to create table and adding all the columns by iterating through the config file"""


def data_entry(data_file):
    f = open("distros.json")
    pass