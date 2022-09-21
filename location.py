import geocoder
import requests
import speech_recognition as sr
import webbrowser
import pyttsx3

def ab(audio):
    print(audio)
    engine = pyttsx3.init()
    engine.say(audio)
    engine.setProperty('rate',160)  #120 words per minute
    engine.setProperty('volume',0.9) 
    engine.runAndWait()
    
g = geocoder.ip('me')
ab(g.latlng)
r = requests.get('https://api.ipdata.co?api-key=test').json()
ab('country : '+r['country_name']+'  city: '+r['city']+ '  network is: '+r['organisation'])
