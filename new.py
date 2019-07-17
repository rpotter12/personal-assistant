import speech_recognition as sr
import os

recognizer = sr.Recognizer()
microphone = sr.Microphone()

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
    if command != 'speak again':
        print(command)
        break