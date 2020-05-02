import sqlite3
import json
from sqlite3 import Error
 
 
def create_connection():
    conn = None
    try:
        conn = sqlite3.connect(':memory:')
        print(sqlite3.version)
        
    except Error as e:
        print(e)

    return conn

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def configure_tables(conn):
    create_users = """ CREATE TABLE IF NOT EXISTS users (
                                    id integer PRIMARY KEY,
                                    name text,
                                    username text,
                                    password text,
                                    address text,
                                    phone text,
                                    tfn INTEGER
                                    ); """

    create_table(conn, create_users)

def initialize_table(conn, table):
    with open(f"./sampledata/{table}.json") as json_file:
      data = json.load(json_file)


    for element in data:
        keylist = []
        valuelist = []
        valuelength = []
        for iter_key, iter_value in element.items():
            keylist.append(str(iter_key))
            valuelist.append(str(iter_value))
            valuelength += "?"
        ### SQL statements in python with dynamic values is a bit unfortunate.
        sql = f'''INSERT INTO {table}({(",".join(map(str, keylist)))}) VALUES({(",".join(map(str, valuelength)))})'''
        print (sql)
        with conn:
            conn.set_trace_callback(print)
            cur = conn.cursor()
            cur.execute(sql, valuelist)

def main():
    global conn 
    conn = create_connection()

    conn.set_trace_callback(print)
    configure_tables(conn)

    initialize_table(conn, "users")

if __name__ == '__main__':
    main()