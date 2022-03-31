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
    column_name = list(data[0].keys())
    f.close()
    print(column_name)
    return column_name
    """a json file is opened with alias f
    data is dumped in data list
    column _name list is made and all keys are inputed using key method"""

def json_column_types(config_file):
    Config_File = open(config_file)
    config = js.load(Config_File)
    column_types = []
    for i in config:
            column_types.append(config[i])
    print(column_types)
    Config_File.close()
    return column_types
    """dbconfig json file is opened and data is loaded into config
    config is iterated over and config[i] is appended to column_types """


def creating_table(config_file):
    f1 = open(config_file)
    config = js.load(config_file)
    cur.execute("CREATE TABLE test('s_no numeric primary key')")
    for i in config:
        cur.execute("ALTER TABLE test ADD COLUMN {} {}".format(i, config[i]))
        con.commit()
    f.close()
""" new function to create table and adding all the columns by iterating through the config file"""


def data_entry(data_file, column_names):
    try:
        f = open("distros.json")
        Data_File = js.load(f)
        for i in Data_File:
            values = list(Data_File.values())
            cur.execute("INSERT INTO test", str(column_names)[1:-1], "VALUES",str(values)[1:-1])
        f.close()
    except Exception as e:
        print(e)
    