#send email to someone function
# for that we have to import smtplib file


# we have to install speech recognization by "pip install SpeechRecognition"

# we also face some error regarding to install pyaudio for that use 
#pip install pipwin
#pipwin install pyaudio

# we also face some error like that if we put same name as wikipedia.py as file name then it can not read that file it show attribute error.


import  pyttsx3
import  datetime
import speech_recognition as sr
import wikipedia
import smtplib


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
   # time()
   # date()

    hour = datetime.datetime.now().hour
    if hour >=6 and hour < 12:
        speak("good morning sir")
    elif hour >=12 and hour < 16:
        speak("good afternoon sir")
    elif hour >=16 and hour < 24:
        speak("good evening sir")
    else:
        speak("good night sir")
        
    speak("Yachika is at your service. How i can help you sir?")
#wishme()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening ....")
        r.pause_threshold = 2 # taking pause for 1 sec adjust yourself
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio,language ='en=IN') # IN used for india we can use any code of any country
        print(query)
    except Exception as e:
        print(e)
        speak("Say that again please ...")

        return "None"

    return query
#takeCommand()

def sendmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)   # 587 is a port number
    server.ehlo()
    server.starttls()  # both commands are used to create a connection
    server.login("uic.20mca1463@gmail.com", "Abhishek@2000")
    server.sendmail("uic.20mca1463@gmail.com", to, content)
    server.close()


if __name__ == "__main__":

    wishme()

    while True:
        query = takeCommand().lower()
        print(query)

        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif "bye" in query:
            quit()
        elif "wikipedia" in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query,sentences = 3)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif "send email" in query:
            try:
                speak("What should I say in email?")
                content = takeCommand()
                to = "xyz@gmail.com"
                sendmail(to, content)
                speak("Email sent successfully")
            except Exception as e:
                speak(e)
                speak("unable to send the message.")

        
            
            
            





