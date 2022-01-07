# importing libraries
import speech_recognition as sr


PATH = 'H:\PycharmProjects\Scrypts\Poligon\SpeechRecognition\8224-274381-0003.flac'

# initialize the recognizer
r = sr.Recognizer()

# open the file
with sr.AudioFile(PATH) as source:
    # listen for the data (load audio to memory)
    audio_data = r.record(source)
    # recognize (convert from speech to text)
    text = r.recognize_google(audio_data)
    print(text)
