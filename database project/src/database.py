# import sqlite3
# import os
# import pypyodbc

# def connect_database():
#     Server= 'DESKTOP-B0GOAL7\SERVER'
#     DATABASE = 'TESTDB'
#     USER = 'sa'
#     PWD = 'abcd1234'
#     data_dir = 'data'
    
#     # Create 'data' directory if it doesn't exist
#     if not os.path.exists(data_dir):
#         os.makedirs(data_dir)
#     constring = 'DRIVER={SQL Server};'+f'SERVER={Server};DATABASE={DATABASE};UID={USER};PWD={PWD};'
#     print(constring)
#     # return sqlite3.connect(f'{data_dir}/database.sqlite')
#     connection = pypyodbc.connect(constring)
#     return connection

import sqlite3
import os

def connect_database():
    data_dir = 'data'
    
    # Create 'data' directory if it doesn't exist
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    return sqlite3.connect(f'{data_dir}/database.sqlite')
