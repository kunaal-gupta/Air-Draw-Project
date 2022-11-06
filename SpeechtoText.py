import pyaudio
import speech_recognition as sr 

r = sr.Recognizer()


with sr.Microphone() as source:
    # read the audio data from the default microphone
    audio_data = r.record(source, duration=5)
    print("Recognizing...")
    # convert speech to text
    text = r.recognize_google(source,key="AIzaSyDRdSN1VaRW27HxA68rZW5FesS2qoPD8", language="fr-FR",show_all=True)

    print(text)