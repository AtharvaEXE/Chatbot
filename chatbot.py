import pyttsx3 
import wikipedia
import speech_recognition as sr
from geopy.geocoders import Nominatim
import str_math
import json

name = "IPS Chat Bot"

engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 20)

def jsonInit():
    questions_file = open(r"question.json", "r")
    questions_str = questions_file.readlines()
    questions = json.loads(questions_str)
    return questions

def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:       
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        print("listening")
        audio = r.listen(source)

    try:
        print("recognizing")
        query = (r.recognize_google(audio, language ='en-in'))      
    except:
        query = "Please repeat it"
        return query

    query.lower()
    print(query)
    return query

def searchWiki(query):
    try:
        search = wikipedia.search(query)
        result = wikipedia.summary(search[0], 2)
    except:       
        result = "sorry, i can not find any results realating to " + query + " on wikipedia"

    print(result)
    return result

def locate(place):
    geolocator = Nominatim(user_agent = "IPS Chat Bot")
    return geolocator.geocode("Taj Mahal", language = "en")

def Greet(engine, name):
    engine.say("Namaste!")
    engine.say("Welcome to IPS")
    engine.say("My name is " + name)
    engine.say("How may I help you")
    engine.runAndWait()

"""
def GetAnswer(query):
    if 'what is your name' in query:
        return 'My name is IPS Chat Bot'
    elif 'what can you do' in query:
        return 'I can answer your simple questions'    
    elif 'are you smart' in query or 'how smart are you in query' in query:
        return 'I am smarter than a toaster'
    elif 'who created you' in query or 'who are your creaters' in query:
        return 'students of class 9 of indore public school created me as a project'
    elif 'how do you work' in query:
        return 'ask my creators'
    else:
        return
"""

Greet(engine, name)

while 1:
    query = takeCommand()
    questions = jsonInit()

    for questions

    if query:
        continue 
    if "what is " in query:
        query = query.replace("what is ", "")
        answer = searchWiki(query)
    
    if "who is " in query:
        query = query.replace("who is ", "")
        answer = searchWiki(query)

    if "where is " in query:
        query = query.replace("where is ", "")
        answer = query + " is located at " + str(locate(query))

    if "thank you" in query:
        answer = "you're welcome"

    engine.say(answer)
    engine.runAndWait()