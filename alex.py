import features
import maps
import responsesGeneric

if __name__ == "__main__":
    
    features.wishme()

    while True:
        query = features.takeCommandCMD().lower()
        
        if 'time' in query:
            features.time()

        #elif 'date' or 'day' in query:
        #    date()

        elif 'send' and 'message' in query:
            try:
                features.speak('To whom do you want to send it?')
                name = features.takeCommandCMD()
                phone = maps.usernames[name]
                features.speak('What is the message?')
                message = features.takeCommandCMD()
                features.sendwppMsg(phone, message)
                features.speak("Consider it done")
            except Exception as e:
                print(e)
                features.speak("Sorry friend, I couldn't send the message")         
            
        elif 'send ' and 'email' in query:

            try:
                features.speak('To whom do you want to send it?')
                name = features.takeCommandCMD()
                receiver = maps.email_list[name]
                features.speak(' What is the subject of the email?')
                subject = features.takeCommandCMD()
                features.speak('and what should I write them?')
                content = features.takeCommandCMD()
                features.sendEmail(receiver,subject,content)
                features.speak("Consider it done")
            except Exception as e:
                print(e)
                features.speak("Sorry friend, I couldn't send the email")

        elif 'wikipedia' in query:
            features.speak('Searching ...')
            query = query.replace('wikipedia', '')
            result = features.wikipedia.summary(query, sentences = 2)
            features.speak(result)
        
        elif "google" in query:
            features.searchGoogle()

        elif "youtube" in query:
            features.speak(features.randomizeResponse(responsesGeneric.youtubeResponses))
            video = features.takeCommandCMD()
            features.pywhatkit.playonyt(video)
            features.speak(features.randomizeResponse(responsesGeneric.amusementIntention))

        elif 'weather' in query:
            city = 'berlin'
            url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid=6e93931106956f35887ca36ad7dc7be4'

            res = features.requests.get(url)
            data = res.json()

            weather = data['weather'] [0] ['main']
            temp = data['main']['temp']
            desp =data['weather'] [0] ['description']
            temp = round((temp - 32) * 5/9)
            features.speak(f'weather in {city} city is like')
            features.speak('Temperature : {} degree celcius'.format(temp))
            features.speak('weather is {}'.format(desp))
        
        elif "news" in query:
            features.news()

        elif "read" in query:
            features.text2speech()

        elif "covid" in query:
            features.covid()

        elif "joke" in query:
            joke = features.pyjokes.get_joke()
            features.speak(joke)

        elif "remember" in query:
            features.speak("What should I remember for you? \n")
            data = features.takeCommandCMD()

            features.speak("I will remember that you said: "+ data)
            remember = open('data.txt', 'w')
            remember.write(data)
            remember.close()
        
        elif "do you know anything" in query:
            remember = open('data.txt', 'r')
            features.speak("You asked me to remember that " + remember.read())

        elif "password" in query:
            features.passwordGen()

        elif "flip a coin" in query:
            features.flipCoin()
        
        elif "roll" in query:
            features.rollDice()
            
        elif "bye" in query:
            features.speak(features.randomizeResponse(responsesGeneric.farewellResponses))
            quit()

        else:
            features.speak(features.randomizeResponse(responsesGeneric.failUnderstandingResponses))       