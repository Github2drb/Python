from pycomm3 import LogixDriver
from typing import List, Dict, Any, Tuple

def read_multiple_tags(plc_ip: str, tags: List[Tuple[str, str]]) -> Dict[str, Any]:
    results = {}
    try:
        with LogixDriver(plc_ip) as plc:
            # Read all tags at once
            tag_results = plc.read(*[tag[0] for tag in tags])
            
            for tag, result in zip(tags, tag_results):
                tag_name, expected_type = tag
                if result.value is not None:
                    results[tag_name] = (result.value, expected_type)
                else:
                    results[tag_name] = (f"Error: {result.error}", "ERROR")
                    
    except Exception as e:
        print(f"An error occurred: {e}")
    
    return results

def interpret_tag_value(tag: str, value: Any, data_type: str) -> str:
    if data_type == "BOOL":
        return "True" if value else "False"
    elif data_type in ["INT", "DINT"]:
        return f"{value}"
    elif data_type == "REAL":
        return f"{value:.2f}"
    elif data_type == "STRING":
        return f"'{value}'"
    else:
        return str(value)

# Replace with your PLC's IP address
plc_ip = '192.168.4.100'

# List of tags to read with their expected data types
tags_to_read = [
    ('EMG_STOP_PB', 'BOOL'),
    ('ST3_HOME_OK', 'Bool'),
    ('OPRM_MSG', 'DINT'),
    ('OPRM_HT_TOP', 'REAL'),
    ('OPRM_HT_BOTTOM', 'REAL')
]

# Read the tags
tag_values = read_multiple_tags(plc_ip, tags_to_read)

# Print the results
#print("Tag Values:")
for tag, (value, data_type) in tag_values.items():
    interpreted_value = interpret_tag_value(tag, value, data_type)
    print(f"{interpreted_value}")

# Additional processing for EMG_STOP_PB
#if "EMG_STOP_PB" in tag_values:
    #emg_stop_value, emg_stop_type = tag_values["EMG_STOP_PB"]
    #if emg_stop_type == "BOOL":
        #if emg_stop_value:
            #print("\nWARNING: Emergency Stop Button is PRESSED!")
        #else:
            #print("\nEmergency Stop Button is not pressed.")
    #else:
        #print(f"\nUnexpected data type for Emergency Stop Button: {emg_stop_type}")