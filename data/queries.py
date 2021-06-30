import sys
from utils.files import import_config

"""Methods for manipulating a SQlite database

Create and insert methods

SQL queries are defined at top of file
"""

# getting database configurations
config = import_config('config_database.json')

# guard clause in case config file doesn't exist
if not config:
    sys.exit(2)

# defining SQL queries
# create_table_query = f'''
#                         CREATE TABLE {config['TABLE_NAME']} (
#                         {config['DATE_COLUMN_NAME']} timestamp NOT NULL PRIMARY KEY,
#                         {config['SECRET_STRING_COLUMN_NAME']} text NOT NULL
#                         );
#                     '''

# # parameterized query to avoid SQL injection
# insert_data_query = f'''
#                         INSERT INTO {config['TABLE_NAME']}
#                         (
#                             {config['DATE_COLUMN_NAME']}, 
#                             {config['SECRET_STRING_COLUMN_NAME']}
#                         ) 
#                         VALUES (?, ?)
#                         ;
#                     '''   

def create_table_query():
    return f'''
                        CREATE TABLE {config['TABLE_NAME']} (
                        {config['DATE_COLUMN_NAME']} timestamp NOT NULL PRIMARY KEY,
                        {config['SECRET_STRING_COLUMN_NAME']} text NOT NULL
                        );
                    '''

def insert_data_query():
    # parameterized query to avoid SQL injection
    return f'''
                        INSERT INTO {config['TABLE_NAME']}
                        (
                            {config['DATE_COLUMN_NAME']}, 
                            {config['SECRET_STRING_COLUMN_NAME']}
                        ) 
                        VALUES (?, ?)
                        ;
                    '''   