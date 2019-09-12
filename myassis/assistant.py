import speech_recognition as sr
from googlesearch import search
import pyttsx3
import os
import spotdl
from gtts import gTTS 

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

recognizer = sr.Recognizer()
microphone = sr.Microphone()

# initialisation for text to speech
# engine = pyttsx3.init() 

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
        print(command)
        return command

def speakvoice(mytext):
    # The text that you want to convert to audio 
    # mytext = 'Welcome Rohit Potter!'
      
    # Language in which you want to convert 
    language = 'en'
      
    # Passing the text and language to the engine,  
    # here we have marked slow=False. Which tells  
    # the module that the converted audio should  
    # have a high speed 
    myobj = gTTS(text=mytext, lang=language, slow=False) 
      
    # Saving the converted audio in a mp3 file named 
    # welcome  
    myobj.save("welcome.mp3") 
      
    # Playing the converted file 
    os.system("mpg321 welcome.mp3")

while True:
    command = command_recog()

    # to tell what command is given
    if command == 'speak again':
        speakvoice(command)

    # to show google search result
    elif "show result for " in command:
    	googlesearchresult(command)
    	continue

    # to get instruction for downloading song
    elif "how to play song " in command:
    	result = "say play song name"
    	print(result)
    	speakvoice(result)
    	continue

    # to play songs
    elif "play" in command:
        command = command + ".mp3"
        speakvoice(command)
        os.system(command)
        continue

    # to download songs
    elif "download song" in command:
        speakvoice("which song you want to download")
        song = command_recog()
        songdownloadcommand = 'spotdl --song "'+song+'"'
        os.system(songdownloadcommand)
        continue

    # to show search result in web browser
    elif "search" in command:
        openwebbrowser(command)
        continue

    elif "exit" in command:
        os.system("exit()")
        break

# method for google search result
def googlesearchresult(wanttosearch):
	query = wanttosearch
	for j in search(query, tld="co.in", num=10, stop=1, pause=2): 
		print(j) 

def openwebbrowser(search):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.google.co.in/")
    wait = WebDriverWait(driver, 600)
    xpath = '//*[@id="tsf"]/div[2]/div/div[1]/div/div[1]/input'
    search_area = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
    search_area.send_keys(search + Keys.ENTER)


