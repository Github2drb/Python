from pycomm3 import LogixDriver
from typing import List, Dict, Any, Tuple
import time
import os

STOP_FILE = "stop_signal.txt"

def read_multiple_tags(plc: LogixDriver, tags: List[Tuple[str, str]]) -> Dict[str, Any]:
    # ... (keep this function as is)

def interpret_tag_value(tag: str, value: Any, data_type: str) -> str:
    # ... (keep this function as is)

def check_stop_signal():
    return os.path.exists(STOP_FILE)

def continuous_read(plc_ip: str, tags_to_read: List[Tuple[str, str]], interval: float = 1.0):
    try:
        with LogixDriver(plc_ip) as plc:
            print("Starting continuous read. Create a file named 'stop_signal.txt' to stop.")
            while not check_stop_signal():
                tag_values = read_multiple_tags(plc, tags_to_read)
                print("\nTag Values:")
                for tag, (value, data_type) in tag_values.items():
                    interpreted_value = interpret_tag_value(tag, value, data_type)
                    print(f"{tag}: {interpreted_value}")
                time.sleep(interval)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if os.path.exists(STOP_FILE):
            os.remove(STOP_FILE)
        print("\nContinuous read stopped.")

# Replace with your PLC's IP address
plc_ip = '192.168.4.100'

# List of tags to read with their expected data types
tags_to_read = [
    ('EMG_STOP_PB', 'BOOL'),
    ('ST3_HOME_OK', 'BOOL'),
    ('OPRM_MSG', 'DINT'),
    ('OPRM_HT_TOP', 'REAL'),
    ('OPRM_HT_BOTTOM', 'REAL')
]

# Start continuous read
continuous_read(plc_ip, tags_to_read, interval=1.0)