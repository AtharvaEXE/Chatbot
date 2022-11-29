# Chatbot
A rule based chatbot

## Required packages

- speech_recognition
- geopy
- wikipedia
- pyttsx3
- word2num
- num2word

## Files [^1]
[^1]: Files which are not mentioned are required for git and are not related to the chatbot

- chatbot.py contains most of the functionality
- strmath.py contains functionality for basic arithmetic
- question.json contains common queries and their replies


## Process

1. The program listens for what the user is saying
2. Processing the audio and understanding what the user is saying by using python speech_recognition module
3. If it finds the query in database, it chooses the corresponding reply
4. If the query is not found in the database
    - If the query is asking about a place it uses geopy module to get the address of that place
    - If the query is asking about a person it uses wikipedia API to get info about the person
    - If the query is asking about a term it uses wikipedia API to get info about the term
5. The program replies with the reply it found using pyttsx3 module 
