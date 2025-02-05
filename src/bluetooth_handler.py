import serial

BLUETOOTH_PORT = "/dev/rfcomm0"  # Change this if needed
BAUD_RATE = 9600

def setup_bluetooth():
    try:
        ser = serial.Serial(BLUETOOTH_PORT, BAUD_RATE)
        print("🔵 Bluetooth connected.")
        return ser
    except Exception as e:
        print(f"❌ Bluetooth connection failed: {e}")
        return None

def receive_command():
    """ Receives a move command via Bluetooth from the Android app """
    ser = setup_bluetooth()
    if ser:
        try:
            data = ser.readline().decode('utf-8').strip()
            return data  # Example: "A2 B6"
        except Exception as e:
            print(f"❌ Error reading Bluetooth data: {e}")
            return None
    return None
