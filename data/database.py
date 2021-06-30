import sqlite3
import datetime
import sys

from data.queries import create_table_query, insert_data_query
from utils.files import import_config

"""Methods for manipulating a SQlite database

Create and insert methods

SQL queries are defined in data/queries.py
"""

# getting database configurations
config = import_config('config_database.json')

# guard clause in case config file doesn't exist
if not config:
    sys.exit(2)

def insert_data_in_database(string):
    """Main method for handling database insert action

    If table doesn't exist it will be created

    Parameters
    ----------
    string : str - 
        string to be inserted
    """
    
    # guard clause in case there is no string
    # this will avoid DB SQL errors
    if string:
        # create table of this is the first run. Consecutive runs will ignore this action
        create_table()

        insert_string_and_timestamp(string)

def create_table():
    """Create SQlite database database/table if it doesn't exist.
    
    If table already exists no action will occur
    Database info comes from config_database.json file
    """

    try:
        print(f"""creating table {config['TABLE_NAME']} if it doesn't already exists""")
        
        # connect to DB and run create table SQL query
        sqliteConnection = sqlite3.connect(config['SQLITE_DATABASE'])
        cursor = sqliteConnection.cursor()
        cursor.execute(create_table_query())
        sqliteConnection.commit()
        cursor.close()

        print(f"""table {config['TABLE_NAME']} created""")

    except sqlite3.Error as error:
        # will print "table <table name> already exists"
        print(error)

    finally:
        if sqliteConnection:
            sqliteConnection.close()


def insert_string_and_timestamp(string: str) -> str:
    """Insert string into table with a corresponding timestamp.

    Parameters
    ----------
    string : str - 
        string to be persisted

    Returns
    ----------
    int - 
        count of database rows inserted. Should be 1 if successfull
    """

    # guard clause is string is None to avoid SQL error later
    if not string:
        print("No string has been found. Exiting")
        sys.exit(2)

    # get current time and date
    timedate = datetime.datetime.now()
    try:
        # connect to DB and run SQL query 
        sqliteConnection = sqlite3.connect(config['SQLITE_DATABASE'])
        cursor = sqliteConnection.cursor()
        query_parameters = (timedate, string)                   # parameterized query values. See SQL query at data/queries.py
        cursor.execute(insert_data_query(), query_parameters)
        sqliteConnection.commit()
        cursor.close()

        row_count = cursor.rowcount
        print("data inserted successfully into table. Lines: ", row_count)
        return row_count

    except sqlite3.Error as error:
        print("failed to insert Python variable into sqlite table", error)

    finally:
        if sqliteConnection:
            sqliteConnection.close()
