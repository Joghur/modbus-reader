import sys
import getopt

from utils.files import import_config

# import CLI options
config = import_config('config_options.json')

def usage():
    return"""
    External device data fetcher
    
    Script for fetching online modbus device data and register it in a SQlite database.
    If a SQlite file doesn't exist it will be created at projects root level. Default name
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

def handle_options(arguments):
    """Method for handling CLI options

    Parameters
    ----------
    arguments : list - 
        list of options and arguments added to CLI command
        
    Returns
    ----------
    str - 
        string of option chosen
    """

    # Handling what happens if script is started with options added
    # There will only be options (like -h or --help) in this script
    # but no arguments like (DEVICE_IP_ADDRESS). This could be added later
    # Don't remove args and argument variables even if not used
    try:
        opts, args = getopt.getopt(
            arguments, config['SHORTHAND_OPTIONS'], config['FULL_OPTIONS'])

    except getopt.GetoptError as error:
        # print help information and exit:
        print(error)
        print(usage())
        sys.exit(2)

    for option, argument in opts:
        # Get the wanted option (in the form of ie. "help" if -help was used)
        # from options_switcher dictionary
        opt = config['OPTIONS_SWITCHER'].get(option)
        return opt