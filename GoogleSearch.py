# try:
#     from googlesearch import search
# except ImportError:
#     print('We cannot find the requested module')
#
#
# query = "Geeksforgeeks"
#
# for data in search(query, tld='ca', lang='en', tbs='0', safe='off', num=10, start=0, stop=None, pause=2.0, country='Canada', extra_params=None, user_agent=None, verify_ssl=True):
# 	print(data)
#
import speech_recognition as sr
import pyttsx3
import pyaudio

r = sr.Recognizer()

def speech_text(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()
    print('bye')


with sr.Microphone() as Source2:
    r.adjust_for_ambient_noise(Source2, duration=0.2)
    audio = r.listen(Source2)
    Mytext = r.recognize_google_cloud(audio)

    print(Mytext)
    print('g')
    speech_text(Mytext)
