import pyttsx3
import datetime
from wikipedia.wikipedia import summary
import maps
import speech_recognition as sr 
import smtplib
from secret import senderemail, epwd, to
from email.message import EmailMessage
import pyautogui
import webbrowser as wb
from time import sleep
import wikipedia
import pywhatkit
import requests
from newsapi import NewsApiClient
import clipboard
import os
import pyjokes
import string
import random
import responsesGeneric

engine = pyttsx3.init() 

def speak(audio):
    voices = engine.getProperty('voices')
    rate = engine.getProperty('rate')
    engine.setProperty("rate", 200)
    engine.setProperty('voice', voices[10].id)
    engine.say(audio)
    engine.runAndWait()
    
def getVoices(voice):
    voices = engine.getProperty('voices')
    #print(voices[0].id)
    if voice == 1:
        engine.setProperty('voice', voices[0].id)
        #speak ("Hello this is male alex")
        
    if voice == 2:
        engine.setProperty('voice', voices[10].id)
        #speak ("Hello this is female alex")
        

def time():
    Time = datetime.datetime.now().strftime("%I:%M") # Hours == I; Minutes == M; Second == S
    speak("Right now is {}".format(Time))
    
def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month )
    date = str(datetime.datetime.now().day )
    speak("Today is {}, {}".format(maps.months[month], date))
    
def greeting():
    hour = datetime.datetime.now().hour
    if hour > 6 and hour < 12:
        return("Good morning friend")
    elif hour >=12 and hour <18:
        return ("Good afternoon friend")
    elif hour >=18 and hour < 24:
        return ("Good evening friend!")
    else:
        return("Good night friend!")


def wishme():
    speak("{}, glad to see you again!\n".format(greeting()))

def takeCommandCMD():
    query = input("How can I help you today?")
    return query

def takeCommandMic():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        
        try:
            print("Recognizing...")
            query = r.recognize_google(audio)
            print(query)
        except Exception as e:
            print(e)
            speak("Can you say that again, please?")
            return "None"
    return query


def sendEmail(receiver, subject, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(senderemail, epwd)
    email = EmailMessage()
    email['From'] = senderemail
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(content)
    server.send_message(email)
    server.close()

def sendwppMsg(phone, message):
    wb.open('https://web.whatsapp.com/send?phone='+phone+'&text='+message)
    sleep(10)
    pyautogui.press('enter')

def searchGoogle():
    speak(randomizeResponse(responsesGeneric.searchGoogleResponses))
    search = takeCommandCMD()
    wb.open('https://www.google.com/search?q='+search)

def news():
    newsapi = NewsApiClient(api_key="3c8fee0965264cdd92b851f2bf63970a")
    speak('What topic are you interested today?')
    topic = takeCommandCMD()
    data = newsapi.get_top_headlines(q = topic, language = "en", page_size = 3)
    newsdata = data['articles']
    for x,y in enumerate(newsdata):
        print(f'{x+1}. {y["description"]}')
        speak((f'{x+1}. {y["description"]})'))
    
    speak(randomizeResponse(responsesGeneric.thatIsAllResponse))
    print(randomizeResponse(responsesGeneric.thatIsAllResponse))


def text2speech():
    text = clipboard.paste()
    if len(text) != 0:
        print(text)
        speak(text)
    else:
        print(randomizeResponse(responsesGeneric.clipboardReadFail))
        speak(randomizeResponse(responsesGeneric.clipboardReadFail))

def covid():
    r = requests.get('https://coronavirus-19-api.herokuapp.com/all')

    data = r.json()
    covidData = f'Confirmed cases: {data["cases"]} \n Deaths : {data["deaths"]} \n Recovered: {data["recovered"]}'

    print(covidData)
    speak(covidData)

def passwordGen():
    s1 = string.ascii_uppercase
    s2 = string.ascii_lowercase
    s3 = string.digits
    s4 = string.punctuation

    passLen = 14
    s = []
    s.extend(s1)
    s.extend(s2)
    s.extend(s3)
    s.extend(s4)

    random.shuffle(s)
    newPass = ("".join(s[0:passLen]))

    print(newPass)
    speak(newPass)

def flipCoin():
    speak(randomizeResponse(responsesGeneric.flipCoinResponses))
    coin = ['heads', ' tails']
    toss = []
    toss.extend(coin)
    random.shuffle(toss)
    toss = ("".join(toss[0]))
    speak(randomizeResponse(responsesGeneric.dramaticRevealResponse) + toss)
    print(randomizeResponse(responsesGeneric.dramaticRevealResponse) + toss)

def rollDice():
    speak(randomizeResponse(responsesGeneric.rollDiceReponses))
    die = ['1', '2', '3', '4', '5', '6']

    roll = []
    roll.extend(die)
    random.shuffle(roll)
    roll = ("".join(roll[0]))
    speak(randomizeResponse(responsesGeneric.dramaticRevealResponse)+ roll)
    print(randomizeResponse(responsesGeneric.dramaticRevealResponse)+ roll)

def randomizeResponse(responses):
    choice = random.randint(0, len(responses)-1)
    return responses[choice]