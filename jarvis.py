import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis. At your service. How can I help you?")


def takeCommand():
    '''
    It takes mictophone input and returns string output
    '''

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recongnizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said:{query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('rklogger0001@gmail.com', 'Rudraksh@143') # more secure method required
    server.sendmail('rklogger0001@gmail.com', to, content)
    server.close()


if __name__ == '__main__':
    wishMe()
    while True:
        quey = takeCommand().lower()

        # logic for execeuting task based on questions

        if 'wikipedia' in quey:
            speak('Searching Wikipedia...')
            query = quey.replace('wikipedia', "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in quey:
            webbrowser.open("youtube.com")

        elif 'open google' in quey:
            webbrowser.open("google.com")
# this can be the best things that we can ever do to make sure this is the best moment in my life to avaoid and work along the workforce to make sure if this is what that can be avoided with some decent caution to make oneself sure
        elif 'open stackoverflow' in quey:
            webbrowser.open("stackoverflow.com")

        elif 'open spotify' in quey:
            webbrowser.open("open.spotify.com")

        elif 'play music' in quey:
            music_dir = 'R:\\webseies'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in quey:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in quey:
            codePath = "C:\\Users\\rudra\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open code' in quey:
            codePath = "C:\\Program Files\\Wondershare\\Wondershare Filmora\\Wondershare Filmora X.exe"
            os.startfile(codePath)

        elif 'open evernote' in quey:
            codePath = "C:\\Users\rudra\\AppData\\Local\\Programs\\Evernote\\Evernote.exe"
            os.startfile(codePath)

        elif 'open obs' in quey:
            codePath = "C:\\Program Files\\obs-studio\\bin\\64bit\\obs64.exe"
            os.startfile(codePath)

        elif 'open notion' in quey:
            codePath = "C:\\Users\\rudra\\AppData\\Local\\Programs\\Notion\\Notion.exe"
            os.startfile(codePath)

        elif 'open android studio' in quey:
            codePath = "C:\\Program Files\\Android\\Android Studio\\bin\\studio64.exe"
            os.startfile(codePath)

        elif 'email to varun' in quey:
            try:
                speak("What should I say?")
                content = takeCommand()

                to = "morevarun4004@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry Master, unable to send the email at this moment")

