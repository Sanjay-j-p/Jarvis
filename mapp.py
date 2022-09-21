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
def mapp():
    print("Listening...")
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source , duration = 1)
        audio2 = r.listen(source)
    query = r.recognize_google(audio2)
    stopwords = ['google', 'maps']
    querywords = query.split()
    resultwords  = [word for word in querywords if word.lower() not in stopwords]
    result = ' '.join(resultwords)
    Chrome = ("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s")
    webbrowser.get(Chrome).open("https://www.google.be/maps/place/"+result+"/")
    rand = [result+'on google maps']
ab('which location do u want to know')
mapp()
