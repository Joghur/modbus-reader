import json

def import_config(file):
    """
    Helper method for importing config files
    """
    try:
        with open(file, 'r') as f:
            config = json.load(f)
            return config

    except FileNotFoundError as error:
        print("File not found", file)