from pycomm3 import LogixDriver
from pycomm3.exceptions import CommError
import time

def monitor_tags(plc, tags, interval=1):
    try:
        while True:
            results = plc.read(tags)
            for tag in results:
                print(f"{tag.tag}: {tag.value}")
            time.sleep(interval)
    except KeyboardInterrupt:
        print("Monitoring stopped")

try:
    with LogixDriver('192.168.1.100') as plc:
        monitor_tags(plc,['EMG_STOP_PB','FLT_RST_PB','FAIL_RST_KS'])
except CommError as e:
    print("Communication Error: {e}")        



