import wolframalpha
import speech_recognition as sr
import webbrowser
import pyttsx3

def abbb(audio):
    print(audio)
    engine = pyttsx3.init()
    engine.say(audio)
    engine.setProperty('rate',160)  #120 words per minute
    engine.setProperty('volume',0.9) 
    engine.runAndWait()
    
def search():
    print("Listening...")
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source , duration = 1)
        audio3 = r.listen(source)
    query = r.recognize_google(audio3)
    client = wolframalpha.Client( "LR7A9E-UQWLJ3QWYH"  )
# get weather forecast
    res = client.query(query)
# print response
    for pod in res.pods:
        for sub in pod.subpods:
            print( sub["plaintext"] )
abbb('what you want to search sir i can get any infomation you want sir:')
search()

