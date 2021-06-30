import sys

# guard clause to make sure python 3 is used
if sys.version_info < (3, 0):
    print("\nRequires Python 3.x, not Python 2.x\n")
    sys.exit(2)

from data.modbus import get_device_string
from data.database import insert_data_in_database
from utils.options import handle_options, usage

"""
    External device data fetcher
    
    Script for fetching online modbus device data and register it in a SQlite database.
    If SQlite file doesn't exist it will be created at projects root level. Default name
    is external_device_data.db. This can be changed in config_database.json (see below).
    Use a SQlite reader to access data.

    Requirements:
     - python 3
     - pymodbus

    Use config files to make changes:
    - config_modbus.json    - IP address, port number, holding register range
    - config_database.json  - Database and table names used. Column names
    - config_options.json   - CLI options

    Options:
    -h or --help:           Helper text

    Examples:
    python3 start.py        # fetch, clean and register data
    python3 start.py --help # helper text
"""

def run(arguments):
    """Main method

    Handles:
     - CLI options
     - Fetching secret string
     - Saving string to database

    Parameters
    ----------
    arguments : list - 
        list of options and arguments added to CLI command
    """
    
    try:
        # if the help CLI option is chosen, print usage help text and exit
        option = handle_options(arguments)
        if option=="help":
            print(usage())
            sys.exit(2)
        
        # fetch string from external device
        secret_string = get_device_string()
        
        # persist string in SQlite database
        insert_data_in_database(secret_string)
        print("\nexit")

    except SystemExit:
        # sys.exit(2) exit commands ends here
        print("\nexit")

    except: 
        print("an unknown error has occured (1)")

if __name__ == "__main__":
    # activate run method with list of arguments
    run(sys.argv[1:])
