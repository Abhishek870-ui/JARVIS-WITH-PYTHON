#wish me function
# here we apply loop so that accoding to time she wish us


import  pyttsx3
import  datetime

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
newVoiceRate = 130
engine.setProperty('rate', newVoiceRate)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#speak("Hello Welcome to all of you for voice assistant jarvis project")

def time():
    Time = datetime.datetime.now().strftime("the current time is  %I:%M:%S")
    speak(Time)

#time()

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)

    speak("the current date is")
    speak(date)
    speak(month)
    speak(year)

#date()

def wishme():
    speak("Welcome back sir!")
    time()
    date()

    hour = datetime.datetime.now().hour
    if hour >=6 and hour < 12:
        speak("good morning sir")
    elif hour >=12 and hour < 16:
        speak("good afternoon sir")
    elif hour >=16 and hour < 24:
        speak("good evening sir")
    else:
        speak("good night sir")
        
    speak("Yachika is at your service")
wishme()

