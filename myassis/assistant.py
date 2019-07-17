import speech_recognition as sr
from googlesearch import search
import pyttsx3
import os
import spotdl

recognizer = sr.Recognizer()
microphone = sr.Microphone()

# initialisation for text to speech
engine = pyttsx3.init() 

# speech recognition function
def command_recog():
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        print('listening...')
        audio = recognizer.listen(source)
        print('processing...')
        try:
            command = recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            return 'speak again'
        return command

while True:
    command = command_recog()

    # to tell what command is given
    if command != 'speak again':
		engine.say(command)

    # to show google search result
    if "show result for " in command:
    	googlesearchresult(command)
    	continue

    # to get instruction for downloading song
    if "how to play song " in command:
    	result = "say play song name"
    	print(result)
    	engine.say(result)
    	engine.runAndWait()
    	continue

    # to play songs
    if "play " in command:
    	command = command + ".mp3"
    	engine.say(command)
    	os.system(command)
    	continue

    # to download songs
    if "download song" in command:
    	engine.say("which song you want to download")
    	song = command_recog()
    	songdownloadcommand = 'spotdl --song "'+song+'"'
    	os.system(songdownloadcommand)
    	continue

# method for google search result
def googlesearchresult(wanttosearch):
	query = wanttosearch
	for j in search(query, tld="co.in", num=10, stop=1, pause=2): 
		print(j) 