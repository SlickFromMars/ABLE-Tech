import pyttsx3
from decouple import config
import speech_recognition as sr
from random import choice
from utils import opening_text
from datetime import datetime
import actions.greet
import actions.input
import actions.online_ops
import actions.os_ops
import requests

USERNAME = config('USER')
BOTNAME = config('BOTNAME')


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
            speak("For your convenience, I am printing it on the screen sir.")
            print(*actions.online_ops.get_trending_movies(), sep='\n')

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
