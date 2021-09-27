# voice option and speak rate
# we can control the voice rate and also the voice communivation of which one come boy/girl
# there are total 6 type of voices
import  pyttsx3
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
newVoiceRate = 120
engine.setProperty('rate', newVoiceRate)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

speak("Hello Welcome to all of you for voice assistant jarvis project")