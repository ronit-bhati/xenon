from tkinter import *
from PIL import Image, ImageTk
import time
import subprocess

root = Tk()
root.title("XENON")
# root.wm_iconbitmap("xenon_icon.ico")
img = ImageTk.PhotoImage(Image.open('xenon_icon.ico'))
root.tk.call('wm', 'iconphoto', root._w, img)

gui_width = 600
gui_height = 400
root.geometry(f"{gui_width}x{gui_height}")
root.minsize(gui_width, gui_height)
root.maxsize(gui_width, gui_height)

heading = Label(root, text="XENON", font="Forte 40", fg="white", bg="#181818")
heading.place(x=200, y=10)

sub_heading = Label(root, text="The most advanced virtual assistant", font="lucida 15 bold", fg="white", bg="#181818")
sub_heading.place(x=125, y=70)


def start():
    global output_screen
    import pyttsx3
    import speech_recognition as sr
    import datetime
    import wikipedia
    import webbrowser
    import os
    import random
    import pywhatkit as kit

    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)

    def speak(audio):
        global output_screen
        engine.say(audio)
        engine.runAndWait()

    def wishMe():
        global output_screen
        hour = int(datetime.datetime.now().hour)

        if 0 <= hour < 12:
            speak("Good Morning!")

        elif 12 <= hour < 17:
            speak("Good afternoon")

        else:
            speak("Good evening")

        speak("I am Xenon! Please tell how may i help you")

    def takeCommand():
        global output_screen

        r = sr.Recognizer()
        with sr.Microphone() as source:
            output_screen.insert(END, 'Listening...\n')
            output_screen.update()
            r.pause_threshold = 1
            r.energy_threshold = 5000
            audio = r.listen(source)
        try:
            output_screen.delete(1.0, END)
            output_screen.insert(1.0, 'Recognizing...\n')
            output_screen.update()
            query = r.recognize_google(audio, language='en-in')
            output_screen.insert(2.0, f"You said: {query}\n")
            output_screen.update()

        except Exception as e:
            output_screen.insert(3.0, 'Say that again please...\n')
            output_screen.update()
            return "None"
        return query

    if __name__ == "__main__":
        wishMe()
        while True:
            query = takeCommand().lower()

            if 'wikipedia' in query:
                speak("Searching Wikipedia...")
                output_screen.delete(1.0, END)
                output_screen.insert(4.0, 'Searching Wikipedia...\n')
                output_screen.update()
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to wikipedia")
                output_screen.insert(5.0, f'According to Wikipedia: {results}\n')
                output_screen.update()
                speak(results)

            elif 'open google' in query:
                speak("Opening Google...")
                webbrowser.open("google.com")

            elif 'google' in query:
                speak("Searching on Google...")
                query = query.replace("google", "")
                kit.search(query)

            elif 'open youtube' in query:
                speak("Opening Youtube...")
                webbrowser.open("youtube.com")

            elif 'play' in query:
                speak("Playing on YouTube...")
                query = query.replace("play", "")
                kit.playonyt(query)

            elif 'open twitter' in query:
                speak("Opening Twitter...")
                webbrowser.open("twitter.com")

            elif 'open instagram' in query:
                speak("Opening Instagram...")
                webbrowser.open("instagram.com")

            elif 'open facebook' in query:
                speak("Opening Facebook...")
                webbrowser.open("facebook.com")

            elif 'open gmail' in query:
                speak("Opening gmail...")
                webbrowser.open("gmail.com")

            elif 'open stack overflow' in query:
                speak("Opening Stack Overflow...")
                webbrowser.open("stackoverflow.com")

            elif 'open omegle' in query:
                speak("Opening omegle.com...")
                webbrowser.open("omegle.com")

            elif 'open quora' in query:
                speak("Opening Quora.com...")
                webbrowser.open("quora.com")

            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"The time is {strTime}")

            elif 'open notepad' in query:
                speak("Opening notepad")
                subprocess.call('notepad.exe')

            elif 'open calculator' in query:
                speak("Opening calculator")
                subprocess.call('calc.exe')

            elif 'open powerpoint' in query:
                speak("Opening powerpoint")
                powerpointPath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
                os.startfile(powerpointPath)

            elif 'open excel' in query:
                speak("Opening excel")
                excelPath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
                os.startfile(excelPath)

            elif 'open word' in query:
                speak("Opening Microsoft Word")
                wordPath = "C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE"
                os.startfile(wordPath)

            elif 'how are you' in query:
                speak("Thanks for asking, i am fine!")

            elif 'you do' in query:
                speak(
                    "I can open web for you or can make a wikipedia search. I can also play music or open     some apps on your pc")

            elif 'name' in query:
                speak("I think i already mentioned it, but anyways, my name is xenon")

            elif 'owner' in query:
                speak("My owner is ronit. You can contact him on instagram @ronit_bhati_")

            elif 'bye' in query:
                speak("Thanks for using me, hope you had a good experience, bye bye!")
                output_screen.delete(1.0, END)
                output_screen.insert(6.0, 'Thanks for using me, hope you had a good experience, byee!\n')
                output_screen.update()
                time.sleep(3)
                from sys import exit
                exit()

            elif 'exit' in query:
                speak("Thanks for using me, hope you had a good experience, bye bye!")
                output_screen.delete(1.0, END)
                output_screen.insert(7.0, 'Thanks for using me, hope you had a good experience, byee!\n')
                output_screen.update()
                time.sleep(3)
                from sys import exit
                exit()

            elif 'hello' in query:
                speak("Hi, how you doin")

            elif 'good' in query:
                speak("Hope, you stay good always")

            elif 'bustard' in query:
                speak("Dont be so rude please")

            elif 'hell' in query:
                speak("Dont be so rude please")

            elif 'kill' in query:
                speak("Dont be so rude please")

            elif 'murder' in query:
                speak("Dont be so rude please")

            else:
                speak("")


logo_run = ImageTk.PhotoImage(Image.open("run.png"))
run = Button(root, image=logo_run, relief=RIDGE, command=start, width=100, height=50)
run.place(x=240, y=115)


def exit_it():
    root.destroy()


quit_func = Button(root, text="Stop", command=exit_it, bg='#181818', fg="white")
quit_func.place(x=280, y=190)

output_screen = Text(root, height=8, font="lucida 13", fg="white", selectborderwidth=0)
output_screen.pack(side="bottom", fill=X, padx=20, pady=10)
output_screen.configure(bg='#181818')

root.configure(bg='#181818')
root.mainloop()
