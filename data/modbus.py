import re
import sys

try:
    from pymodbus.client.sync import ModbusTcpClient as ModbusClient
except ImportError as error:
    print(error, "is installed. Use 'pip install -U pymodbus' to install") # error if modbus is not installed
    sys.exit(2)
    
from utils.files import import_config

# import modbus configurations
config = import_config('config_modbus.json')

# guard clause in case config file doesn't exist
if not config:
    sys.exit(2)

def get_device_string():
    """main data method handling all data related actions

    - Fetches data from external device
    - Convert to ASCII characters
    - Return trimmed string
    """

    try:
        holding_registers = fetch_external_device_data()
        
        converted_to_ASCII = convert_to_ASCII(holding_registers)

        # concat list into one string, trim #'s away and return
        return trim_sharp_from_string(''.join(converted_to_ASCII))

    except: 
        print("an unknown error has occured (2)")

def fetch_external_device_data():
    """Fetches modbus data

    Modbus info as IP address and Port is found in config_modbus.json

    Returns
    ----------
    list - 
        list of holding register 16bit integers
    """

    # connect to modbus device using info from config
    client = ModbusClient(config['MODBUS_SERVER_IP'], port=config['MODBUS_SERVER_PORT'])
    client.connect()

    # read holding registers from ie. 0 to 100. 
    request = client.read_holding_registers(config['HOLDING_REGISTER_MIN'], config['HOLDING_REGISTER_MAX'])

    # checking if there was an error
    assert(not request.isError())

    result = request.registers

    client.close()

    return result

def convert_to_ASCII(unconverted_register_list):
    """Convert list of integer codes to ASCII characters

    Parameters
    ----------
    unconverted_register_list : list - 
        list to be converted

    Returns
    ----------
    list - 
        list of converted ASCII characters
    """

    converted_list = []
    for element in unconverted_register_list:
        if isinstance(element, int):            # check if element is an integer
            ascii = chr(element)
            converted_list.append(ascii)

    return converted_list

def trim_sharp_from_string(string):
    """Removes # characters from string

    Parameters
    ----------
    string : str - 
        string to be trimmed

    Returns
    ----------
    list - 
        list of converted ASCII characters
    """

    if string:
        # Remove all #'s from string and return
        return re.sub("#", "", string) 
