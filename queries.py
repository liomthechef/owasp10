import sqlite3
import json
import database
import pandas as pd
from sqlite3 import Error
 
def query_user(datasource, username):
    conn = database.conn

    query_cur = conn.cursor()
    query_cur.execute("SELECT * FROM users WHERE username='{cv}'".\
            format(cv=username))
    result = query_cur.fetchall()

    return result
    
# def search_columns(key, value, datasource):
#     conn = database.conn
#     query_cur = conn.cursor()
#     query_cur.execute("SELECT * FROM {tn} WHERE {cn}='{cv}' COLLATE NOCASE".\
#             format(tn=datasource, cn=key, cv=value))
#     id_exists = query_cur.fetchall()
#     print(id_exists)

#     return id_exists

# def search_id_user(key, value, datasource):
#     conn = database.conn
#     query_cur = conn.cursor()
#     query_cur.execute("SELECT * FROM users INNER JOIN tickets ON users._id = tickets.assignee_id WHERE users._id={cv} COLLATE NOCASE".\
#             format(tn=datasource, cn=key, cv=value))
#     id_exists = query_cur.fetchall()
#     print(pd.DataFrame(id_exists))
#     return id_exists


def main():
   database.main() 

   output = query_user("users", "georges OR 1=1")
   print (output)

if __name__ == '__main__':
    main()