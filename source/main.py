#!/usr/bin/env python
import socket
# from pocketsphinx import LiveSpeech
import speech_recognition as sr


TCP_IP = '127.0.0.1'
TCP_PORT = 1025
BUFFER_SIZE = 1024
MESSAGE = "append1([a,b], c, X)."

def actions():
    m = sr.Recognizer()
    with sr.Microphone() as source:
        audio = m.listen(source)
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY", show_all=True)`
        # instead of `r.recognize_google(audio, show_all=True)`
        userinput = m.recognize_google(audio).split(' ')
        for count, data in enumerate(userinput):
            if count < len(userinput)-1:
                userinput[count] = data + ', '
        print('\n\n\nSUCCESS\n\n\nWill send the following term to prolog\n')
        sendstream = "inputparser([" + ''.join(userinput) + "], X)."
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((TCP_IP, TCP_PORT))
        s.send(sendstream)
        data = s.recv(BUFFER_SIZE)
        s.close()
        print("received data:", data)
    except sr.UnknownValueError:
        print("Assistant could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
            audio = r.listen(source)
    try:
        if r.recognize_google(audio) == 'hey assistant' or r.recognize_google(audio) == 'his system' or r.recognize_google(audio) == 'hey system' or r.recognize_google(audio) == 'his assistant' or r.recognize_google(audio) == 'assistance' or r.recognize_google(audio) == 'assistant':
            print("\n\n\nSUCCESS! \n\n\nThis is assistant. How can I be of service?")
            actions()
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY", show_all=True)`
        # instead of `r.recognize_google(audio, show_all=True)`
    except sr.UnknownValueError:
        print("Assistant could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))