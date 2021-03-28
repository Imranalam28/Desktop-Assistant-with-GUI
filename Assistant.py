import pyttsx3
import datetime
import pyjokes
import smtplib
import time
import speech_recognition as sr
import psutil
import os
import webbrowser
import wikipedia
from tkinter import *

window = Tk()

engine = pyttsx3.init()

voice = engine.getProperty('voices')

time1 = ''



def speak(audio):

    engine.say(audio)
    engine.runAndWait()

def current_time():
    time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("Current time is ")
    speak(time)

def date():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    speak(day)
    speak(month)
    speak(year)

def setting():
    new = Toplevel(window)
    new.title("Settings")
    new.geometry("300x300")
    c1 = Checkbutton(new,text="Show Time",font=('Arial',10,'bold'),onvalue=1,offvalue=0,command=tktime)
    c1.place(x=100,y=150)

def cpu():
    cpu_usage = str(psutil.cpu_percent())
    print(cpu_usage)
    speak('cpu is at' + cpu_usage)

def boy():
    engine.setProperty('voice',voice[0].id)

def girl():
    engine.setProperty('voice',voice[1].id)

def Email(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('demouserpython@gmail.com','python@123')
    server.sendmail('demouserpython@gmail.com',to,content)
    server.close()

def battery():
    battery_usage = str(psutil.sensors_battery())
    print(battery_usage)
    speak('battery is at' + battery_usage)

def tktime():
    global time1
    time2 = datetime.datetime.now().strftime('%H:%M:%S %p')
    if time2 != time1:
        time1 = time2
        label3.config(text = time2)

    label3.after(200,tktime)


def exit():
    quit()

def greet():
    hour = datetime.datetime.now().hour

    if hour>= 6 and hour < 12:
        speak("Good morning sir!")

    elif hour >= 12 and hour < 18:
        speak("Good afternoon sir!")

    elif hour >= 18 and hour < 24:
        speak("Good evening sir!")

    else:
        speak("Good night sir!")

def jokes():
    joke = pyjokes.get_joke()
    print(joke)
    speak(joke)

def Command():
    s = sr.Recognizer()
    with  sr.Microphone() as source:
        print("Listening...")
        s.pause_threshold = 1
        audio = s.listen(source)

    try:
        print("Recognizing...")
        command = s.recognize_google(audio,language= 'en-US')
        print(command)
        speak(command)

    except Exception as e:
        print(e)
        speak("say that again please")
        return "None"

    return command

def run():
    greet()
    check = True

    while check:
        command = Command().lower()

        if 'date' in command:
            date()
        #elif 'day' in command:

        elif 'time' in command:
            current_time()

        elif 'joke' in command:
            jokes()

        elif 'go offline' in command:
            speak("Going offline sir")
            check = False

        elif 'stop listening' in command:
            speak("For how many seconds you want me to stop listening to your commands?")
            ans = int(input())
            speak(ans)
            speak("seconds ok sir!")
            time.sleep(ans)

        elif 'cpu' in command:
            cpu()

        elif 'battery' in command:
            battery()

        elif 'open spotify' in command:
            speak("opening spotify")
            spotify = r'C:\Users\MY PC\AppData\Roaming\Spotify\Spotify.exe'
            os.startfile(spotify)

        elif 'search in youtube' in command:
            speak("what you want to search?")
            search = Command().lower()

            webbrowser.open('https://www.youtube.com/results?search_query=' + search)

        elif 'search in google' in command:
            speak("What you want to search?")
            chromeloc = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe%s"
            search = Command().lower()
            webbrowser.get(chromeloc).open_new_tab(search + '.com')

        elif 'send email' in command:
            try:
                speak("what you want to send?")
                content = Command()
                to = input("Enter reciever's email id")
                Email(to,content)
                print(content)
                speak("Email has been sent sir")

            except Exception as e:
                print(e)
                speak("unable to send email")

        elif 'wikipedia' in command:
            speak("Searching")
            command = command.replace('wikipedia','')
            command = command.replace('search','')
            command = command.replace('in','')
            result = wikipedia.summary(command,sentences=2)
            speak("According to wikipedia")
            print(result)
            speak(result)

            
window.title("Desktop Assistant")
window.geometry("1000x1000")
window.config(bg='black')

bg = PhotoImage(file = ".\images.png")

label2 = Label(window,image=bg,bg='black',fg='white')
label2.place(x=120,y=80)
label3 = Label(window,font=('calibri',25,'bold'),bg = 'black',fg='white')
label3.place(x=20,y=620)
label4 = Label(window,font=('Arial',25,'bold'),text='D.A',bg='black',fg='white')
label4.place(x=390,y=290)



label1 = Label(window,text="Destop Assistant",font=('Arial',40),bg = 'black',fg = 'white')
label1.pack()

r1 = Radiobutton(window,text="Boy",font=('Arial',30),value=0,command=boy,bg = 'black',fg = 'blue')
r1.pack(anchor = W)
r2 = Radiobutton(window,text="Girl",font=('Arial',30),value=1,command=girl,bg = 'black',fg = 'blue')
r2.pack(anchor = W)

b1 = Button(window,text='Start',font=('Arial',32),command=run).place(x=680,y=500)
b2 = Button(window,text='Exit',font=('Arial',32),command=exit).place(x=686,y=600)
b3 = Button(window,text='Settings',command=setting,font=('Arial',32)).place(x=680,y=400)

window.mainloop()
            

