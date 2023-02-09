from ast import Break
from asyncio import subprocess
from re import search
from gtts import gTTS
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import sys
import wolframalpha


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am AI . Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...") 
        speak("can u repeat that") 
        return "None"
    return query

def note(audio):
    date=datetime.datetime.now()
    file_name=str(date).replace(":","-")+"-note.txt"
    with open(file_name,"w") as f:
        f.write(audio)
    subprocess.Popen(["notepad.exe",file_name])


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("what should i open in google")
            cm=takeCommand().lower()
            webbrowser.open(f"{cm}")
            #webbrowser.open("google.com")
        elif 'open games' in query:
            speak("opening games")
            power = r"C:\Games"
            os.startfile(power)

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   

        elif 'search'  in query:
            query = query.replace("search", "")
            webbrowser.open(query)   

        elif "camera" in query or "take a photo" in query:
            ec.capture(0,"robo camera","img.jpg")

        elif 'play music' in query:
            speak("opening spotify")
            webbrowser.open("https://open.spotify.com/collection/tracks")
        
        elif 'open word document' in query:
            speak("opening word document")
            power = r"C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office 2013\\Word 2013"
            os.startfile(power)
        
        elif 'open desktop' in query:
            speak("opening desktop")
            power = r"C:\Users\NIKSH\OneDrive\Desktop"
            os.startfile(power)
        
        elif 'open program files' in query:
            speak("opening program files")
            power = r"C:\\Program Files"
            os.startfile(power)
        
        elif 'open folders' in query:
            speak("opening folders")
            power = r"C:\Users\NIKSH\OneDrive\Desktop\FOLDER"
            os.startfile(power)
        
        elif 'c drive' in query:
            speak("opening c drive")
            power = r"C:\\"
            os.startfile(power)
        

        elif 'open notepad' in query:
            speak("opening notepad")
            power = r"C:\Program Files\Notepad++\notepad++.exe"
            os.startfile(power)
        
        elif 'quit' in query or 'abort' in query or 'bye' in query or 'stop' in query:
            speak("quitting")
            sys.exit()

        elif 'maths' in query or 'one more' in query:
            speak('hello what do u need help at?')
            question=takeCommand()
            app_id="TJ87G9-WYLTKXT63G"
            client = wolframalpha.Client('TJ87G9-WYLTKXT63G')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer),
            print(answer)

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak("the time is {strTime}")

        elif 'open python' in query:
            speak("opening python")
            codePath = "C:\\Users\\RMTar\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Anaconda3 (64-bit)\\Spyder (anaconda3)"
            os.startfile(codePath)

        elif "hello" in query:
            from pywikihow import search_wikihow
            speak("hello how can i help you")
            how = takeCommand()
            max_results = 1
            how_to =search_wikihow(how,max_results)
            assert len(how_to) == 1
            how_to[0].print()
            speak(how_to[0].summary)

        elif 'email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "nikkybunny74@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry i am not able to send this email")    
