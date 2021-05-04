import pyttsx3
import datetime
import maps
import speech_recognition as sr 

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
    if voice == 2:
        engine.setProperty('voice', voices[10].id)

    speak ("Hello this is alex")


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
    speak("{}, glad to see you again! What can we do together today?\n".format(greeting()))

#while True:
#voice = int(input("Press 1 for male and 2 for female voice\n"))
#    speak(audio)

#getVoices(voice)

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
        query = r.recognize_google(audio, language='en-US')
        print(query)
    except Exception as e:
        print(e)
        speak("Can you say that again, please?")
        return "None"
    return query

if __name__ == "__main__":
    wishme()

    while True:
        query = takeCommandMic().lower()
        if 'time' in query:
            time()

        elif 'date' or 'day' in query:
            date()
            
        else:
            speak("I didn't quite get it. Can you repeat please?")



            