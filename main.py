import speech_recognition as sr
import pyttsx3
import openai
import os
from dotenv import load_dotenv

# Load API key from the 'openai.env' file
load_dotenv("openai.env")
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('volume', 0.9)  # Volume level (0.0 to 1.0)

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to recognize speech from the microphone
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
            return None
        except sr.RequestError:
            print("Request error from Google Speech Recognition.")
            return None

# Function to handle user commands using GPT-3.5 or GPT-4
def process_command(command):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # You can change to "gpt-4" if you have access
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": command}
            ],
            max_tokens=100
        )
        reply = response['choices'][0]['message']['content']
        print(f"Assistant: {reply}")
        speak(reply)
    except Exception as e:
        print(f"Error: {e}")
        speak("There was an error processing your command.")

# Main function to run the voice assistant
def main():
    speak("Hello! How can I assist you today?")
    while True:
        command = recognize_speech()
        if command:
            if "exit" in command or "quit" in command:
                speak("Goodbye!")
                break
            else:
                process_command(command)

if __name__ == "__main__":
    main()