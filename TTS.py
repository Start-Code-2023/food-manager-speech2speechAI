import speech_recognition as sr
from pynput import keyboard
from gtts import gTTS
import time
import os
from pydub import AudioSegment
from pydub.playback import play

import OpenAI.gpt as gpt

# Initialize the recognizer
recognizer = sr.Recognizer()
is_listening = False
  
def on_key_release(key):
    global is_listening
    if key == keyboard.Key.f10:                                                    
        if is_listening:
            is_listening = False
            print("Stopped listening")
        else:
            is_listening = True
            print("Started listening")

# Set up the keyboard listener
listener = keyboard.Listener(on_release=on_key_release)
listener.start()

# Function to convert text to speech
def text_to_speech(text, language="en"):  
    tts = gTTS(text, lang=language)
    tts.save("output.mp3")

    # Wait until the file is saved
    while not os.path.exists("output.mp3"):
        time.sleep(0.1)
    
    # Use aplay to play the audio (you can replace with mpg123 or another player)
    audio = AudioSegment.from_mp3("output.mp3")
    play(audio)

    # Delete the file after playing
    os.remove("output.mp3")
  
# Use a microphone as the audio source                     
with sr.Microphone() as source:
    while True:
        if is_listening:
            norwegian_text = ""
            print("Please start speaking...")
            audio = recognizer.listen(source)

            # Recognize the speech for both English and Norwegian
            try:        
                # Recognize as Norwegian
                norwegian_text = recognizer.recognize_google(audio, language="nb-NO")  
                print(f"You said: {norwegian_text}")

                user_message = {
                    "role": "user",
                    "content":  norwegian_text
                }

                gpt_response = gpt.get_gpt_response(user_message)

                text_to_speech(gpt_response, language="no")
                print("\nAI Said: " + gpt_response)

            except sr.UnknownValueError:
                print("Sorry, I couldn't understand the audio.")
            except sr.RequestError as e:   
                print(f"Sorry, there was an error with the request: {e}")
