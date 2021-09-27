#speak function
# speak function help to call the function again and again to speak the jarvis
# First of all we have to install pyttsx3 for that use "pip install pyttsx3"

import  pyttsx3
engine = pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    speak("this is friday")

