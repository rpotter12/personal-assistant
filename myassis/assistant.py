import speech_recognition as sr
from googlesearch import search
import pyttsx3
import os, glob
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

# speech recognition function(for speech to text)
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

# for text to speech
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

# method for google search result
def googlesearchresult(wanttosearch):
	for j in search(wanttosearch, tld="co.in", num=10, stop=1, pause=2): 
		print(j) 

# open web browser and search results on it
def openwebbrowser(search):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.google.co.in/")
    wait = WebDriverWait(driver, 600)
    xpath = '//*[@id="tsf"]/div[2]/div/div[1]/div/div[1]/input'
    search_area = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
    search_area.send_keys(search + Keys.ENTER)

# load all song into a file
def load_all_songs():
	global ALL_SONGS
	ALL_SONGS = [] 
	song = glob.glob("/home/rohit/Music/*")
	for i in song:
		ALL_SONGS.append(i)

# delete all song from the list
def del_all_songs():
	for i in All_SONGS:
		ALL_SONGS.remove(i)

# find song in the list
def find_song(name):
	for i in ALL_SONGS:
		if name.lower() in i.lower():
			temp_name = i.split("/home/rohit/music/")
			name = temp_name[-1]
			return name

load_all_songs()

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
	elif "play song" in command:
		speakvoice("which song you want to play")
		song = command_recog()
		newsong=find_song(song)

		"""
		# method to search the exact name of the searched song
		path="/home/rohit/Music/"
		song_list = os.listdir(path)
		print(song_list)
		i=0
		length=len(song_list)
		newsong = "abc"
		for i in range(0,length):
			if song in song_list[i].lower():
				newsong = song_list[i]
		"""

		print(newsong)

		command = "xdg-open \"" + newsong + "\""
		speakvoice(command)
		os.system(command)
		continue

	# to download songs
	elif "download song" in command:
		speakvoice("which song you want to download")
		song = command_recog()
		songdownloadcommand = 'spotdl --song "'+song+'"'
		os.system(songdownloadcommand)
		del_all_songs() #empty whole list
		load_all_songs() #append all song in songs file after downloading
		continue

	# to show search result in web browser
	elif "search" in command:
		openwebbrowser(command)
		continue

	# to exit from the software
	elif "exit" in command:
		os.system("exit()")
		break

