import RPi.GPIO as GPIO
import time

# Define motor and electromagnet pins
X_STEP_PIN = 17
Y_STEP_PIN = 27
MAGNET_PIN = 22

# Setup GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(X_STEP_PIN, GPIO.OUT)
GPIO.setup(Y_STEP_PIN, GPIO.OUT)
GPIO.setup(MAGNET_PIN, GPIO.OUT)

def move_piece(command):
    print(f"♟️ Moving piece: {command}")
    start, end = command.split()  # Example: "A2 B6"

    # Convert chess notation to X-Y coordinates
    start_x, start_y = convert_to_coordinates(start)
    end_x, end_y = convert_to_coordinates(end)

    # Move to starting position
    move_to(start_x, start_y)
    activate_magnet(True)  # Pick up piece

    # Move to end position
    move_to(end_x, end_y)
    activate_magnet(False)  # Drop piece

def convert_to_coordinates(position):
    """ Convert chess notation (A2, B6) to X-Y coordinates """
    column = ord(position[0].upper()) - 65  # A=0, B=1, ..., H=7
    row = int(position[1]) - 1  # Convert 1-8 to 0-7
    return column, row

def move_to(x, y):
    print(f"🚀 Moving to X: {x}, Y: {y}")
    GPIO.output(X_STEP_PIN, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(Y_STEP_PIN, GPIO.HIGH)
    time.sleep(0.5)

def activate_magnet(state):
    GPIO.output(MAGNET_PIN, GPIO.HIGH if state else GPIO.LOW)
    print("🧲 Magnet Activated" if state else "🧲 Magnet Deactivated")
