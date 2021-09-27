#time function
# time function is used to tell us time 

import  pyttsx3
import  datetime

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
newVoiceRate = 120
engine.setProperty('rate', newVoiceRate)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

speak("Hello Welcome to all of you for voice assistant jarvis project")

def time():
    Time = datetime.datetime.now().strftime("the time is now %I:%M:%S")
    speak(Time)

time()