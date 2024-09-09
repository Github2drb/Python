from pymodbus.client import ModbusTcpClient
from pymodbus.exceptions import ModbusIOException
import time

# Connect to the cooling unit
client = ModbusTcpClient('192.168.1.100', port=502)

# Attempt to connect
if not client.connect():
    print("Failed to connect to the Modbus server.")
else:
    try:
        # Read the current temperature (example register address)
        result = client.read_holding_registers(address=100, count=1, unit=1)
        
        if not result.isError():
            temperature = result.registers[0] / 10.0  # Assuming temperature is stored as tenths of a degree
            print(f"Current temperature: {temperature}°C")
        else:
            print("Error reading registers:", result)

    except ModbusIOException as e:
        print("Modbus IO Exception:", e)
    except Exception as e:
        print("An unexpected error occurred:", e)
    finally:
        # Close the connection
        client.close()