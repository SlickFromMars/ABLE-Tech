import webbrowser
import time
import datetime
from frame.Remember import yourname
import frame.Structure

# import frame.Structure


def speakprint(text):
    print(text)
    # frame.Structure.speak(text)


def wishme():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speakprint("Good morning, " + yourname)
    elif hour < 18:
        speakprint("Good afternoon, " + yourname)
    else:
        speakprint("Good evening, " + yourname)


myname = 'ABLE'

wishme()

if __name__ == '__main__':

    while True:
        statement = frame.Structure.takeCommand()
        # statement = input("Enter your command: ").lower()
        statement = statement.lower()
        if statement == 0:
            continue

        if "good bye" in statement or "ok bye" in statement or "stop" in statement:
            speakprint(myname + ' is shutting down, good bye.')
            break

        elif 'search' in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)

        elif statement == 'rickroll':
            webbrowser.open_new_tab('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

        elif 'who are you' in statement or 'what can you do' in statement:
            speakprint('I am ' + myname + ', an AI created by master Slick.')
            speakprint('ABLE stands for Artifical Buddy Lacking Entity')
            speakprint('Get it? Because you are my only buddy?')
