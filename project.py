import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime 
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib

engine=pyttsx3.init('sapi5') #to use inbuilt voice by microsoft(to know more search sapi5)
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<17:
        speak("Good Afternoon!")
    elif hour>=17 and hour<20:
        speak("Good Evening!")
    else:
        speak("Hello Sir")

    speak("Hi,I am Sam. Please tell me how may I help you")

def takeCommand():
    #it takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio=r.listen(source)#to know about listen and threshold source use ctrl+click

    try:
        print("Recognizing....")
        query=r.recognize_google(audio, language='en-in') #to know about recognize google source use ctrl+click
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please....")
        return "None"
    return query

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('rewantpandey1999@gmail.com','rewant12353')
    server.sendmail('rewantpandey1999@gmail.com',to,content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        query=takeCommand().lower()
        #logic for executing task based on query
        if 'wikipedia' in query:
            speak("searching wikipedia....Please Wait....")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=1)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("opening youtube ...")
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            speak("opening google...")
            webbrowser.open("google.com")
        
        elif 'open linkedin' in query:
            speak("opening linkedin...")
            webbrowser.open("linkedin.com")

        elif 'open facebook' in query:
            speak("opening facebook...")
            webbrowser.open("facebook.com")

        elif 'play music' in query:
            speak("playing music...")
            musicPath='C:\\Users\\Rewant Pandey\\Desktop\\python\\projects\\AI Project\\song2.mpeg'
            os.startfile(musicPath)

        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,The time is {strTime}")

        elif 'open code' in query:
            speak("opening code...")
            codePath="C:\\Users\\Rewant Pandey\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        
        elif 'send email' in query:
            try:
                speak("What Should I say?")
                content=takeCommand()
                to="rewantparashar@gmail.com"
                sendEmail(to,content)
                speak("Ok Sir Your Email has been sent!")
            
            except Exception as e:
                print(e)
                speak("I am sorry sir.I am not able to send the email to rewant")

        elif 'quit' in query:
            speak("My work is Done here Sir")
            speak("I am Quitting..")
            exit() 

            
