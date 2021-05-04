import pyttsx3
import datetime
import maps

engine = pyttsx3.init() 

def speak(audio):
    engine.setProperty("rate", 220)
    engine.setProperty("voice", 4)
    engine.say(audio)
    engine.runAndWait()
    
def getVoices(voice):
    voices = engine.getProperty('voices')
    #print(voices[0].id)
    if voice == 1:
        engine.setProperty('voice', voices[0].id)
    if voice == 2:
        engine.setProperty('voice', voices[4].id)

    speak ("Hello this is alex")


def time():
    Time = datetime.datetime.now().strftime("%I:%M") # Hours == I; Minutes == M; Second == S
    speak("Right now is {}".format(Time))
    
def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month )
    date = str(datetime.datetime.now().day )
    speak("Today is {}, {}".format(maps.months[month], date))
    
#while True:
#voice = int(input("Press 1 for male and 2 for female voice\n"))
#    speak(audio)

#getVoices(voice)
