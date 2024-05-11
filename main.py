import nltk
import nltk.data
import os
from datetime import datetime
import time
import pywhatkit
import datetime
import pyttsx3
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import speech_recognition as sr
import keyboard

keyboard.press_and_release('ctrl+w') # closes the last tab
recognizer = sr.Recognizer()

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[1].id)

now = datetime.datetime.now()
hour = now.hour

def main():
    with sr.Microphone() as source:
        print("I am your Sky, How can I help You")
        engine.say("I am your Sky, How can I help You..., What would you like ? save your data or would like to start talking with me ?")
        engine.runAndWait()

        recordedaudio = recognizer.listen(source)
        text = recognizer.recognize_google(recordedaudio, language='en-us')
        print(text)
        if 'save' in text:
            #print("ready to store")
            import getInfo
        elif 'start' in text:
            #print("start")
            import extractINFO
        elif 'bye' in text:
            engine.say("Good Bye Nidhi")
            engine.runAndWait()
            exit()
        else:
            print("try again")

main()











