# -*- coding: utf-8 -*-
"""
Created on Wed June 5 07:58:06 2020

@author: Sanjay
"""

from gtts import gTTS
import speech_recognition as sr
import os
import webbrowser
import smtplib
from playsound import playsound
import pyttsx3
from time import strftime
import sys
import re

from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
from weather import Weather
import pyowm
import importlib
from PyDictionary import PyDictionary
import wmi
import psutil
import time


def talkToMe(audio):
    print(audio)
    engine = pyttsx.init()
    engine.say(audio)
    engine.setProperty('rate',149)  #120 words per minute
    engine.setProperty('volume',0.9) 
    engine.runAndWait()



#listens for commands
    
def mycommand():
    
    r=sr.Recognizer()
    
    with sr.Microphone() as source:
        print('Listening....sir:')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source , duration = 1)
        audio = r.listen(source)
        
    try:
        command=r.recognize_google(audio)
        print('you said :' + command + '/n')
    
    except sr.UnknownValueError:
       command = mycommand()
       
    return command

def assistant(command):
    
    #website
    if 'open website' in command:
        reg_ex = re.search('open website (.+)', command)
        if reg_ex:
            domain = reg_ex.group(1)
            url = 'https://www.' + domain +'.com'
            webbrowser.open(url)
            print('Done!')
        else:
            pass
    elif 'jarvis' in command or 'Jarvis' in command:
        talkToMe("Yes sir")
    elif 'calculate' in command or 'wolf' in command or 'search' in command:
        import calc
        a=0
        a=a+1
        if a==0:
            importlib.reload(calc)
    elif 'brightness control' in command or 'brightness' in command:
        talkToMe('do you want it to be low brightness  or medium or increase')
        r=sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(source , duration = 1)
            audio5 = r.listen(source)
        query1 = r.recognize_google(audio5)
        if 'low brightness' in query1:
            dec = wmi.WMI(namespace='wmi')
            methods = dec.WmiMonitorBrightnessMethods()[0]
            methods.WmiSetBrightness(20, 0)
        elif 'medium' in query1:
            dec = wmi.WMI(namespace='wmi')
            methods = dec.WmiMonitorBrightnessMethods()[0]
            methods.WmiSetBrightness(50, 0)
        else:
            dec = wmi.WMI(namespace='wmi')
            methods = dec.WmiMonitorBrightnessMethods()[0]
            methods.WmiSetBrightness(100, 0)
    #greetings
    elif 'my IP address' in command:
        webbrowser.open('http://checkip.dyndns.com/')
    elif 'my location' in command or 'current location' in command:
        import location
        k=0
        k=k+1
        if k==0:
            importlib.reload(location)
    elif 'jarvis are you there' in command:
        talkToMe('at your service sir')
    elif 'Google search' in command or 'Google' in command:
        import google
        l=0
        l=l+1
        if l==0:
            importlib.reload(google)
    elif 'music' in command or 'Music' in command:
        import music
        p=0
        p=p+1
        if p==0:
            importlib.reload(music)
    elif 'Youtube search' in command or 'YouTube/n' in command:
        import youtube
        l=0
        l=l+1
        if l==0:
            importlib.reload(youtube)
    elif 'drive' in command:
        reg_ex = re.search('drive (.+)', command)
        if reg_ex:
            domain = reg_ex.group(1)
            os.system('explorer ' + domain + ':\\'.format(''))
            print('Done!')
        else:
            pass
    elif 'charge' in command:
            battery = psutil.sensors_battery()
            plugged = battery.power_plugged
            percent = int(battery.percent)
            
            talkToMe(str(percent)+ r'  percentage')
            if percent < 40 and plugged == False:
                talkToMe('sir, please connect charger because i can survive only ')
            if percent < 40 and plugged == True:
                talkToMe("don't worry, sir charger is connected")
            else:
                talkToMe('sir, no need to connect the charger because i can survive ' )
            
    elif 'hello Jarvis' in command or 'hello' in command or 'hi there' in command:
        day_time = int(strftime('%H'))
        if day_time < 12:
            talkToMe('Hello Sir. Good morning')
        elif 12 <= day_time < 18:
            talkToMe('Hello Sir. Good afternoon')
        else:
            talkToMe('Hello Sir. Good evening')
            
    elif 'what is the date and time' in command or 'time and date' in command:
        talkToMe(datetime.now().strftime('%Y-%m-%d %H:%M:%S')+'  sir')
        
    elif 'tell me a joke' in command:
        res = requests.get('https://icanhazdadjoke.com/',headers={"Accept":"application/json"})
        if res.status_code == requests.codes.ok:
            talkToMe(str(res.json()['joke']))
        else:
            talkToMe('oops!I ran out of jokes')
            
    elif 'open weather' in command:
        import rweatherr
        j=0
        j=j+1
        if j==0:
            importlib.reload(rweatherr)
        
        print("hh")
    elif 'open map' in command:
        
        import mapp
        i=0
        i=i+1
        if i==0:
            importlib.reload(mapp)
        
        
            
    elif 'shutdown' in command or 'shut up' in command:
           
           talkToMe('Bye Sir, have a good day.')
           get_ipython().magic('reset -sf')
           get_ipython().magic('clear')
           import sys
           sys.exit()
    #top stories from google news
    elif 'news for today' in command:
        try:
            news_url="https://news.google.com/news/rss"
            Client=urlopen(news_url)
            xml_page=Client.read()
            Client.close()
            soup_page=soup(xml_page,"html.parser")
            news_list=soup_page.findAll("item")
            # Print news title, url and publish date
            a=0
            for news in news_list:
                
                a=a+1
                if(a>7):
                    break
                else:
                    talkToMe(news.title.text)
                    talkToMe(news.link.text)
                    print("-"*60)
        except Exception as e:
                print(e)
        
    else:
            talkToMe('I don\'t know what you mean!')

time.sleep(3)
talkToMe('sir I am ready for your command')

#loop to continue executing multiple commands
while True:
    assistant(mycommand())
