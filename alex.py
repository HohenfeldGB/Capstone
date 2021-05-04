import pyttsx3

engine = pyttsx3.init() 

def speak(audio):
    
    engine.say(audio)
    engine.runAndWait()
    
while True:
    audio = input("Enter the text to convert to speech\n")
    speak(audio)