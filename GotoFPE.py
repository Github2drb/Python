from zk import ZK, const
import time

# Configuration
ip = '192.168.4.201'  # Replace with your device's IP address
port = 4370  # Default port for ZKTeco devices

def switch_to_enrollment_screen():
    zk = ZK(ip, port=port, timeout=5)
    conn = None
    
    try:
        conn = zk.connect()
        print(f"Connection to {ip} successful")

        # Disable the device before sending commands
        conn.disable_device()

        # Send command to switch to enrollment mode
        conn.set_user_enroll_status(1)
        print("Command sent to switch to enrollment screen")

        # Some devices might require additional commands or a delay
        time.sleep(2)

        # You might need to send additional commands here, depending on your device model

        print("Device should now be in enrollment mode")
        print("Please check the device screen")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        if conn:
            # Re-enable the device
            conn.enable_device()
            conn.disconnect()
            print("Disconnected from device")

if __name__ == "__main__":
    switch_to_enrollment_screen()