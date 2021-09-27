#text to speech
# this help to speak the text which is written in the code speak by the jarvis
# First of all we have to install pyttsx3 for that use "pip install pyttsx3"

import  pyttsx3
engine = pyttsx3.init()
engine.say("hello world")
engine.runAndWait()
