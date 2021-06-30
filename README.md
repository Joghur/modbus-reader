# Modbus reader

External device data fetcher
    
Script for fetching online modbus device data and register it in a SQlite database.  

If a SQlite file doesn't exist it will be created at the projects root level. Default name is **external_device_data.db**. This can be changed in **config_database.json** (see below).  

Use a SQlite reader to access data.


## IMPORTANT
Before use change IP address/port in **config_modbus.json** to relevant values.

---

### Requirements:  
- **python 3**
- **pymodbus**

---
### Configs
Use config files to make changes:
- **config_modbus.json**    - IP address, port number, holding register range
- **config_database.json**  - Database and table names used. Column names
- **config_options.json**   - CLI options

---
### CLI options:  
**-h** or **--help**:        Helper text

### Examples:  
**python3 start.py**        # fetch, clean and register data  
**python3 start.py --help** # helper text