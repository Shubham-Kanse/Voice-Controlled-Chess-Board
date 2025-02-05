import speech_recognition as sr

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening for a command...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio)  # Convert speech to text
            return command
        except sr.UnknownValueError:
            print("❌ Could not understand the command.")
            return None
        except sr.RequestError:
            print("❌ Speech recognition service is unavailable.")
            return None
