import speech_recognition as sr
import pyttsx3
from weather import Weather
import pyowm
def abb(audio):
    print(audio)
    engine = pyttsx3.init()
    engine.say(audio)
    engine.setProperty('rate',160)  #120 words per minute
    engine.setProperty('volume',0.9) 
    engine.runAndWait()
def weatherr():
        owm = pyowm.OWM('enter your own weather token id')
        print('Listening.....')
        r=sr.Recognizer()
        with sr.Microphone() as source:
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(source , duration = 1)
            audio1 = r.listen(source)
        observation = owm.weather_at_place(r.recognize_google(audio1))
        w = observation.get_weather()
        abb(w.get_temperature('celsius')['temp'])
abb('which location do u want to know the weather')
weatherr()
