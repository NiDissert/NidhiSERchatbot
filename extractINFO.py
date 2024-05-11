import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
recognizer = sr.Recognizer()
import file
import keyboard
import wikipedia
keyboard.press_and_release('ctrl+w') # closes the last tab
ni = "1"
#Extracted Values - stored by user
name = file.Name
city = file.Favourite_City
morningAct = file.morning
afternoonAct = file.afternoon
nightAct = file.night
ingoodTalk = file.goodMoodTalk
inbadTalk = file.badMoodTalk
fsong = file.sadSong
dSong = file.danceSong
rsong = file.relaxSong
neu = file.possitiveZone


engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[1].id)

#Get Time and start with greeting as per time
now = datetime.datetime.now()
hour = now.hour

if hour < 12:
    greeting = "Good morning"
    gnrl = morningAct
    quote = "In the morning time..."
elif hour < 18:
    greeting = "Good Afternoon"
    gnrl = afternoonAct
    quote = "In the afternoon..."
else:
    greeting = "It's a beautiful night"
    gnrl = nightAct
    quote = "Hope you had great day today... at time of sleeping"

#General greeting as per time
engine.say(greeting)
engine.runAndWait()
engine.say("I am glad... to assist you")
engine.runAndWait()
#engine.say(quote)
#engine.say(gnrl)
engine.runAndWait()

engine.say("Anyways..., let's start to talk something else")
engine.say("How is the day today ? ... May I give you suggestion ? ")
engine.runAndWait()

#get input to assist user as per mood
while True:
    with sr.Microphone() as source:
        recordedAudio1 = recognizer.listen(source)
        text1 = recognizer.recognize_google(recordedAudio1, language='en-us')
        print(text1)

    Sentence = [str(text1)]
    analyser = SentimentIntensityAnalyzer()
    for i in Sentence:
        v = analyser.polarity_scores(i)

    if 'suggestion' in text1 or 'yes' in text1:
        engine.say("Ok then let me have a look on your like and dislikes")
        engine.say(quote)
        engine.say(gnrl)
        engine.runAndWait()
        if v['compound'] >= 0.05:
           # print("Positive")
           engine.say(ingoodTalk)
           engine.runAndWait()
        elif v['compound'] <= - 0.05:
        #print("Negative")
            engine.say(inbadTalk)
            engine.runAndWait()
        else:
            #print("Neutral")
            engine.say(neu)
            engine.runAndWait()
    elif 'music' in text1 and 'favourite' in text1:
        print("favourite song")
        pywhatkit.playonyt(fsong)
    elif 'music' in text1 and 'calm' in text1:
        print("Calm song")
        pywhatkit.playonyt(rsong)
    elif 'music' in text1 and 'dance' in text1:
        print("Dance song")
        pywhatkit.playonyt(dSong)
    elif 'city' in text1:
        detail = wikipedia.summary(city)
        engine.say(detail)
        engine.runAndWait()
    elif 'bye' in text1:
        engine.say("Good Bye" + name)
        engine.runAndWait()
        exit()
    elif text1 is None:
        engine.say("Let's have a talk please... will have fun")
        engine.runAndWait()
    else:
        print("try")

