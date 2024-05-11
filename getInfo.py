import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[1].id)

def data():
    with sr.Microphone() as source:
        name = print("Your Name Please")
        engine.say("What is your sweet Name Please")
        engine.runAndWait()
        recordedaudio = recognizer.listen(source)
        txtName = recognizer.recognize_google(recordedaudio, language='en-us')

        city = print("Your city name")
        engine.say("City Please")
        engine.runAndWait()
        recordedaudio = recognizer.listen(source)
        txtCity = recognizer.recognize_google(recordedaudio, language='en-us')

        morning = print("How you would like to staet your day ?")
        engine.say("How you would like to staet your day ?")
        engine.runAndWait()
        recordedaudio = recognizer.listen(source)
        txtmor = recognizer.recognize_google(recordedaudio, language='en-us')

        afternoon = print("How you would like to spend your work in afternoon")
        engine.say("How you would like to spend your work in afternoon")
        engine.runAndWait()
        recordedaudio = recognizer.listen(source)
        txtNoon = recognizer.recognize_google(recordedaudio, language='en-us')

        night = print("Can you please tell me your favourite bed time activity ?")
        engine.say("Can you please tell me your favourite bed time activity ?")
        engine.runAndWait()
        recordedaudio = recognizer.listen(source)
        txtNight = recognizer.recognize_google(recordedaudio, language='en-us')

        talkGood = print("Who is that guy with whom you love to talk when you are in good mood")
        engine.say("Who is that guy with whom you love to talk when you are in good mood")
        engine.runAndWait()
        recordedaudio = recognizer.listen(source)
        txt_talkGood = recognizer.recognize_google(recordedaudio, language='en-us')

        talkBad = print("Who is that great guy who always hekps you in your anxiety or any problem  ?")
        engine.say("Who is that great guy who always hekps you in your anxiety or any problem  ?")
        engine.runAndWait()
        recordedaudio = recognizer.listen(source)
        txt_talkBad = recognizer.recognize_google(recordedaudio, language='en-us')

        sadSong = print("which song you preffer to listen when you are sad ?  ?")
        engine.say("which song you preffer to listen when you are sad ?  ?")
        engine.runAndWait()
        recordedaudio = recognizer.listen(source)
        txt_sadSong = recognizer.recognize_google(recordedaudio, language='en-us')

        danceSong = print("Tell me the song which made you dance")
        engine.say("Tell me the song which made you dance")
        engine.runAndWait()
        recordedaudio = recognizer.listen(source)
        txt_danceSong = recognizer.recognize_google(recordedaudio, language='en-us')

        relaxSong = print("To be a relax what you would like to listen ???")
        engine.say("To be a relax what you would like to listen ???")
        engine.runAndWait()
        recordedaudio = recognizer.listen(source)
        txt_relaxSong = recognizer.recognize_google(recordedaudio, language='en-us')

        relaxSong = print("When you feel possitive vibes ? ???")
        engine.say("When you feel possitive vibes around you...")
        engine.say("When you are feeling full energatic... full on mood")
        engine.say("what you prefer to do ...???")
        engine.runAndWait()
        recordedaudio = recognizer.listen(source)
        txt_positive = recognizer.recognize_google(recordedaudio, language='en-us')




        with open('file.py', 'a') as file:
            # write variables using repr() function
            file.write("Name = " + repr(txtName) + '\n')
            file.write("Favourite_City = " + repr(txtCity) + '\n')
            file.write("morning = " + repr(txtmor) + '\n')
            file.write("afternoon = " + repr(txtNoon) + '\n')
            file.write("night = " + repr(txtNight) + '\n')
            file.write("goodMoodTalk = " + repr(txt_talkGood) + '\n')
            file.write("badMoodTalk = " + repr(txt_talkBad) + '\n')
            file.write("sadSong = " + repr(txt_sadSong) + '\n')
            file.write("danceSong = " + repr(txt_danceSong) + '\n')
            file.write("relaxSong = " + repr(txt_relaxSong) + '\n')
            file.write("possitiveZone = " + repr(txt_positive) + '\n')
data()

