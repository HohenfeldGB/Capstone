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
    speak('what should i search?')
    search = takeCommandCMD()
    wb.open('https://www.google.com/search?q='+search)

def news():
    newsapi = NewsApiClient(api_key="3c8fee0965264cdd92b851f2bf63970a")
    speak('What topic are you interested today?')
    topic = takeCommandCMD()
    data = newsapi.get_top_headlines(q = topic, language = "en", page_size = 5)
    newsdata = data['articles']
    for x,y in enumerate(newsdata):
        print(f'{x+1}. {y["description"]}')
        speak((f'{x+1}. {y["description"]})'))
    
    speak("That's all we got for now. Ask me for new updates in the near future")


def text2speech():
    text = clipboard.paste()
    if len(text) != 0:
        print(text)
        speak(text)
    else:
        print("You have nothing in your clipboard, try to copy the text you want me to read")
        speak("You have nothing in your clipboard, try to copy the text you want me to read")

def covid():
    r = requests.get('https://coronavirus-19-api.herokuapp.com/all')

    data = r.json()
    covidData = f'Confirmed cases: {data["cases"]} \n Deaths : {data["deaths"]} \n Recovered: {data["recovered"]}'

    print(covidData)
    speak(covidData)

if __name__ == "__main__":
    
    wishme()

    while True:
        query = takeCommandCMD().lower()
        if 'time' in query:
            time()

        #elif 'date' or 'day' in query:
        #    date()

        elif 'send' and 'message' in query:
            try:
                speak('To whom do you want to send it?')
                name = takeCommandCMD()
                phone = maps.usernames[name]
                speak(' What is the message?')
                message = takeCommandCMD()
                sendwppMsg(phone, message)
                speak("Consider it done")
            except Exception as e:
                print(e)
                speak("Sorry friend, I couldn't send the message")            
            
        elif 'send ' and 'email' in query:

            try:
                speak('To whom do you want to send it?')
                name = takeCommandCMD()
                receiver = maps.email_list[name]
                speak(' What is the subject of the email?')
                subject = takeCommandCMD()
                speak('and what should I write them?')
                content = takeCommandCMD()
                sendEmail(receiver,subject,content)
                speak("Consider it done")
            except Exception as e:
                print(e)
                speak("Sorry friend, I couldn't send the email")

        elif 'wikipedia' in query:
            speak('Searching ...')
            query = query.replace('wikipedia', '')
            result = wikipedia.summary(query, sentences = 2)
            print (result)
            speak(result)

        elif "youtube" in query:
            speak("What video would you like to see?")
            video = takeCommandCMD()
            pywhatkit.playonyt(video)
            speak("that sounds interesting")

        elif 'weather' in query:
            city = 'chicago'
            url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid=6e93931106956f35887ca36ad7dc7be4'

            res = requests.get(url)
            data = res.json()

            weather = data['weather'] [0] ['main']
            temp = data['main']['temp']
            desp =data['weather'] [0] ['description']
            temp = round((temp - 32) * 5/9)
            print(weather)
            print(temp)
            print(desp)    
            speak(f'weather in {city} city is like') 
            speak('Temperature : {} degree celcius'.format(temp))
            speak('weather is {}'.format(desp))
        
        elif "news" in query:
            news()

        elif "read" in query:
            text2speech()



        elif "covid" in query:
            covid()
        elif "offline" or "bye" or "goodbye" in query:
            speak("See you soon!")
            quit()

        



        else:
            speak("I didn't quite get that. Can you repeat please?")
        


            