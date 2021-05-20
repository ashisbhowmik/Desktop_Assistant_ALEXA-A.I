import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
from datetime import date
import wikipedia
import pyjokes
import webbrowser
import os


listener = sr.Recognizer()
engine = pyttsx3.init()

# convert alexa tone into female voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        talk("Good Morning Sir!")
    elif hour > 12 and hour < 18:
        talk("Have a good day sir!")
    else:
        talk("I wish to have a good Night with sweet dream Sir")


def open(order):
    talk('Opening' + order)
    webbrowser.open("www." + order + ".com")


def talk(text):
    engine.say(text)
    engine.runAndWait()


talk('what can i do for you sir')


def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()

            if 'alexa' in command:
                command = command.raplace('alexa', '')
                print(command)

    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)

    if 'play' in command:
        song = command.replace('play', '')
        pywhatkit.playonyt('playing' + song + 'from youtube')
        talk('playing song in youtube')
        print('playing...')

    # elif 'open vs code' in command:
    #     openpath = 'C:\\Users\\HP\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
    #     os.startfile(openpath)
    #     talk('opening Visual Studio Code')

    # elif 'back to homepage' in command:
    #     openpath = 'C:\\Users\\HP\\OneDrive\Desktop\\PYTHON PROGRAMME WITH CODE TOTAL\\All Project Python\\Alexa Aplication\\main.py'
    #     os.startfile(openpath)
    #     talk('Returning you into the home page of your project')

    # elif 'open excel' in command:
    #     openpath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
    #     os.startfile(openpath)
    #     talk('Opening Ms Excel')

    # elif 'open camera' in command:
    #     openpath = "C:\\Program Files (x86)\\CyberLink\\YouCam6\\YouCam6.exe"
    #     os.startfile(openpath)
    #     talk('Opening Camera')

    # elif 'open photoshop' in command:
    #     openpath = '"C:\\Program Files (x86)\\Adobe\\Photoshop 7.0\\Photoshop.exe"'
    #     os.startfile(openpath)
    #     talk('opening Adobe Photoshop in your windows')

    elif 'stop' in command:
        talk('quitting the programe')
        talk(wishMe())
        exit()

    elif 'open youtube' in command:
        open('youtube')

    elif 'open google' in command:
        open('google')

    elif 'open facebook' in command:
        open('facebook')

    elif 'open instagram' in command:
        open('instagram')

    elif 'open twitter' in command:
        open('twitter')

    elif 'open wikipedia' in command:
        open('widipedia')

    elif 'open linkedin' in command:
        open('linkedin')

    elif 'open github' in command:
        open('github')

    # elif 'open website' in command:
    #     talk('opening ashisbhowmik.com')
    #     webbrowser.open("localhost/forum2")

    elif 'name' in command:
        talk('My name is Alexa.. I am now your desktop assistence')

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('current time is ' + time)

    elif 'what' in command:
        person = command.replace('what', '')
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info)

    elif 'search' in command:
        person = command.replace('search', '')
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info)

    elif 'who' in command:
        person = command.replace('who', '')
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info)

    elif 'when' in command:
        person = command.replace('when', '')
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info)

    elif 'joke' in command:
        a = pyjokes.get_joke()
        print(a)
        talk(a)

    elif 'date' in command:
        today = date.today()
        calender = today.strftime("%B %d, %Y")
        print("Today's  date:", calender)
        talk('Sir, everyday is  very beautiful, but today' +
             calender + ' is a special day for you')

    elif 'hello' in command:
        talk('Hello Sir, I am your alexa assistance, you can ask any question to me, like tell me date, time, search ,play music in youtube, who is the person, tell me a joke etc')

    elif 'love' in command:
        talk('Of Course sir, if you don"t have any girlfriend, then i definitely love you')

    elif 'date with' in command:
        talk('no sir, I can"nt go to a date with you because i have a important meeting')

    else:
        talk("Sorry Sir, Please said this again")


while True:
    run_alexa()
