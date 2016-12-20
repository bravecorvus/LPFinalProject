#!/usr/bin/env python
from datetime import datetime
import subprocess
import httplib2
import os
from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
import datetime
import socket
import speech_recognition as sr

dalist = []
# the list to check potential months against
monthlist = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
# create the year list to check against
yearcalendar = []
for i in range(1900, 2100):
    yearcalendar.append(str(i))
# set up communication link to communicate with SWI-Prolog
TCP_IP = '127.0.0.1'
TCP_PORT = 1025
BUFFER_SIZE = 1024

# Google Calendar API Magic
def get_credentials():
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'calendar-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def readoutnextevent():
    try:
        import argparse
        flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
    except ImportError:
        flags = None
    SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'
    CLIENT_SECRET_FILE = 'client_secret.json'
    APPLICATION_NAME = 'Google Calendar API Python Quickstart'
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)

    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    eventsResult = service.events().list(
        calendarId='primary', timeMin=now, maxResults=10, singleEvents=True,
        orderBy='startTime').execute()
    events = eventsResult.get('items', [])

    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        dastring = start + ' ' + event['summary']
        dalist.append(dastring)
    subprocess.call(["espeak", dalist[0][26:]])
# If nothing else, it will read back exactly what you said
def simpleread(arg):
    subprocess.call(["espeak", arg])    

# main function that pulls out useful information out of the "set(calendar event)" return call from Prolog
def languageparser(arg):
    splitstring = arg.split(' ')
    print(splitstring)
    for count, data in enumerate(splitstring):
        if data in monthlist:
            print(data)
            month = data
    for count, data in enumerate(splitstring):
        if data in yearcalendar:
            year = data
# checks for term "a.m."
    for count, data in enumerate(splitstring):
        if data== "a.m.":
            try:
                if splitstring[count-2] not in yearcalendar:
                    hours = splitstring[count-2]
                    minutes = splitstring[count-1]
                    seconds = "00"
                elif splitstring[count-1] not in yearcalendar:
                    hours = splitstring[count-1]
                    minutes = "00"
                    seconds = "00"
            except:
                hours = splitstring[count-1]
                minutes = "00"
                seconds = "00"
# checks for term "p.m."
        elif data== "p.m.":
            try:
                if splitstring[count-2] not in yearcalendar:
                    temp = int(splitstring[count-2]) + 12
                    hours = str(temp)
                    minutes = splitstring[count-1]
                    seconds = "00"
                elif splitstring[count-1] not in yearcalendar:
                    temp = int(splitstring[count-1]) + 12
                    hours = str(temp)
                    minutes = "00"
                    seconds = "00"
            except:
                temp = int(splitstring[count-1]) + 12
                hours = str(temp)
                minutes = "00"
                seconds = "00"
# checks for term "o'clock"
        elif data == "o'clock":
            try:
                hours = splitstring[count-1]
                minutes = "00"
                seconds = "00"
            except:
                print("o'clock except")
                continue
    # clean up splitstring
    try:
        splitstring.remove(hours)
    except:
        print("\n")
    try:
        splitstring.remove(minutes)
    except:
        print("\n")
    try:
        splitstring.remove("o'clock")
    except:
        print("\n")
    try:
        splitstring.remove("p.m.")
    except:
        print("\n")
    try:
        splitstring.remove("a.m.")
    except:
        print("\n")
    try:
        splitstring.remove(month)
    except:
        print("\n")
    try:
        splitstring.remove(year)
    except:
        print("\n")
    for count, data in enumerate(splitstring):
        try:
            # look for day's (e.g. 31st)
            if data[-2:] == "st" or data[-2:] == "nd" or data[-2:] == "rd" or data[-2:] == "th":
                # print(data[:-2])
                int(data[:-2])
                day = data[:-2]
                dayindex = count
        except:
            continue
        try:
            splitstring.remove(splitstring[dayindex])
        except:
            continue
    try:
        splitstring.remove("p.m.")
    except:
        print("\n")
    try:
        splitstring.remove("a.m.")
    except:
        print("\n")
    content = ' '.join(splitstring)
    print(content)
    print("\n")
    print(month)
    print("/")
    print(day)
    print("/")
    print(year)
    print(hours)
    print(":")
    print(minutes)
    print(":")
    print(seconds)
    print("\n")




def setcalendar(arg):
    datlist = languageparser(arg) #datlist will look like [2016-12-25-20:00:00, "dinner with jennifer"]

# funcparser parses the entire return from SWI-Prolog 
# In essence, it's the "action" arm of the program
def funcparser(arg):
    if arg == "get(next, calender, event)":
        readoutnextevent()
    # elif arg look like set(dinner with jennifer december 25, 2016)
    elif arg[:6] == "create":
        setcalendar(arg[7:])
    elif arg[:3] == "set":
        setcalendar(arg[4:])
    else:
        simpleread(arg)


def actions(): #once the program recognizes the phrase "hey assistant" it will listen for userinput, then send it to the prolog interpreter
    m = sr.Recognizer()
    with sr.Microphone() as source:
        audio = m.listen(source)
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY", show_all=True)`
        # instead of `r.recognize_google(audio, show_all=True)`
        userinput = m.recognize_google(audio).split(' ')
        for count, data in enumerate(userinput):
            userinput[count] = userinput[count].encode("utf-8")
        # convert the google audio into a string
        sendstream = ' '.join(userinput)
        print('\n\n\nSUCCESS\n\n\nWill send the following term to prolog\n')
        print(sendstream)
        print(type(sendstream))
        # create a new socket to send string to SWI-Prolog
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # connect and send sendstream
        s.connect((TCP_IP, TCP_PORT))
        s.send(bytes(sendstream).encode('utf-8'))
        # receive data from SWI-Prolog
        data = s.recv(BUFFER_SIZE)
        print("\n\n\n\nWE GOT DATA BACK FROM PROLOG\n\n\n")
        print(data)
        s.close()
        funcparser(data)
    except sr.UnknownValueError:
        print("Assistant could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

# int main() {
while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
            audio = r.listen(source)
    try:
        # use google voice api to recognize audio, and covert it to text
        googleaudio = r.recognize_google(audio)
        # multiple checks (since all the following words can be mistakenly recognized instead of "hey assitant")
        if googleaudio == 'hey assistant' or googleaudio == 'his system' or googleaudio == 'hey system' or googleaudio == 'his assistant' or googleaudio == 'assistance' or googleaudio == 'assistant':
            print("\n\n\nSUCCESS! \n\n\nThis is assistant. How can I be of service?")
            actions()
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY", show_all=True)`
        # instead of `r.recognize_google(audio, show_all=True)`
    except sr.UnknownValueError:
        print("Assistant could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))