import subprocess
import platform
from concurrent.futures import ThreadPoolExecutor

def check_ip_connection(ip_address):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, '1', ip_address]
    
    try:
        subprocess.check_output(command, stderr=subprocess.STDOUT, timeout=2)
        return ip_address, True
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired):
        return ip_address, False

ip_addresses = [
    "192.168.4.220",
    "192.168.4.221",
    "192.168.4.225",
    "192.168.4.233",
    "192.168.4.234",
    "192.168.4.20"
]

with ThreadPoolExecutor() as executor:
    results = dict(executor.map(check_ip_connection, ip_addresses))

for ip, status in results.items():
    print(f"{ip}: {status}")