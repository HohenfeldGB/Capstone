import pyttsx3

engine = pyttsx3.init() 

def speak(audio):
    
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

while True:
    voice = int(input("Press 1 for male and 2 for female voice\n"))
#    speak(audio)

    getVoices(voice)