import time
import speech_recognition as sr
import bluetooth_handler
import motor_control
import game_logic

def main():
    print("🎙️ Voice-Controlled Chess Board Initialized...")

    while True:
        print("Waiting for a command...")
        command = bluetooth_handler.receive_command()  # Receive move command from Android app

        if command:
            print(f"Received Command: {command}")

            if game_logic.validate_move(command):  # Check if move is valid
                motor_control.move_piece(command)  # Move the chess piece
                print("✅ Move executed successfully!")
            else:
                print("❌ Invalid move. Please try again.")

        time.sleep(2)  # Delay before next command

if __name__ == "__main__":
    main()
