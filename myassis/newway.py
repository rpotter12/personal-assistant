# import os
# os.system("echo 'hello world'")
# os.system("say 'hello world'")

import pyttsx3
engine = pyttsx3.init()

engine.say("Your Text")

engine.runAndWait()