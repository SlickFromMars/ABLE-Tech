import pyttsx3
from decouple import config
import speech_recognition as sr
from random import choice
from utils import opening_text
from datetime import datetime
import actions.greet
import actions.online_ops
import actions.os_ops

USERNAME = config('USER')
BOTNAME = config('BOTNAME')

MUTED = 0


engine = pyttsx3.init('sapi5')

# Set Rate
engine.setProperty('rate', 190)

# Set Volume
engine.setProperty('volume', 1.0)

# Set Voice (Female)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


# Text to Speech Conversion
def speak(text):
    """Used to speak whatever text is passed to it"""

    print(text)
    if MUTED == 0:
        engine.say(text)
        engine.runAndWait()


def take_user_input():
    """Takes user input, recognizes it using Speech Recognition module and converts it into text"""

    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print('Listening....')
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print('Recognizing...')
            query = r.recognize_google(audio, language='en-in')
            if not 'exit' in query or 'stop' in query:
                speak(choice(opening_text))
            else:
                hour = datetime.now().hour
            if hour >= 21 and hour < 6:
                speak("Good night sir, take care!")
            else:
                speak('Have a good day sir!')
            exit()
        except Exception:
            speak('Sorry, I could not understand. Could you please say that again?')
            query = 'None'
    except Exception:
        query = input('Input command: ')
    return query


if __name__ == '__main__':

    actions.greet.greet_user()
    while True:
        query = take_user_input().lower()

        if 'open project expansion' in query:
            speak("Opening Project Expansion in the Unreal Editor now.")
            actions.os_ops.open_project()

        elif "trending movies" in query:
            speak(f"Some of the trending movies are: {actions.online_ops.get_trending_movies()}")

        elif 'my ip address' in query:
            ip_address = actions.online_ops.find_my_ip()
            speak(f'Your IP Address is {ip_address}.\n For your convenience, I am printing it on the screen sir.')
            print(f'Your IP Address is {ip_address}')

        elif 'joke' in query:
            speak(f"Hope you like this one sir")
            joke = actions.online_ops.get_random_joke()
            speak(joke)
            print(joke)

        elif 'weather' in query:
            ip_address = actions.online_ops.find_my_ip()
            speak("For which city shall I get the weather?")
            city = input("Choose City: ")

            try:
                weather, temperature, feels_like = actions.online_ops.get_weather_report(city)
                speak(f"The current temperature is {temperature}, but it feels like {feels_like}")
                speak(f"Also, the weather report talks about {weather}")
                print(f"Description: {weather}\nTemperature: {temperature}\nFeels like: {feels_like}")
            except Exception:
                speak("Sorry sir, I could not find the weather.")

        elif 'open command prompt' in query:
            actions.os_ops.open_cmd()
            speak("Opening command prompt now sir.")

        elif 'rickroll me' in query:
            speak("Enjoy the song, sir.")
            actions.online_ops.rick_roll()

        elif 'toggle mute' in query:
            speak("Toggling mute, sir.")
            if MUTED == 0:
                MUTED = 1
            else:
                MUTED = 0

        elif 'mute' in query:
            if MUTED == 0:
                speak("Muting now sir.")
                MUTED = 1
            else:
                speak("I am already muted sir.")

        elif 'unmute' in query:
            if MUTED == 1:
                MUTED = 0
                speak("Unmuting now sir.")
            else:
                speak("I am already unmuted sir.")

        else:
            speak("There was no action associated with your command.")
