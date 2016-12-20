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
monthlist = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
TCP_IP = '127.0.0.1'
TCP_PORT = 1025
BUFFER_SIZE = 1024

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

def simpleread(arg):
    subprocess.call(["espeak", arg])    

def languageparser(arg):
    month = ""
    day = ""
    year = ""
    content = ""
    time = ""
    splitstring = arg.split(' ')
    for count, data in enumerate(splitstring):
        if data in monthlist:
            month = data
    for count, data in enumerate(splitstring):
        if data[-2:] == "PM" or data[-2:] == "AM":
            time = data
    for count, data in enumerate(splitstring):
        if data[:4] == "2016" or data[:4] == "2017":
            year = data
    limitlist = arg
    try:
        limitlist.remove(time)
    except:
        print("\n")
    try:
        limitlist.remove(month)
    except:
        print("\n")
    try:
        limitlist.remove(year)
    except:
        print("\n")
    for i in limitlist:
    try:
        int(i) #testing to see if there are any other integers
        day = i
    except:
        continue
    try:
        limitlist.remove(day)
    except:
        print("\n")
    content = ' '.join(limitlist)
    timedaylist = []
    try:
        timedaylist.append(month)
        timedaylist.append(day)
        timedaylist.append(year)
        timedaylist.append(time)
    except
        timedaylist.append(month)
        timedaylist.append(day)
        timedaylist.append('2016')
        timedaylist.append(time)
    timeday = ' '.join(timedaylist)
    datetime_object = datetime.strptime(timeday, '%B %d %Y %I:%M%p')
    print(datetime_object)




def setcalendar(arg):
    datlist = languageparser(arg) #datlist will look like [2016-12-25-20:00:00, "dinner with jennifer"]

def funcparser(arg):
    if arg == "get(next, calender, event)":
        readoutnextevent()
    # elif arg look like set(dinner with jennifer december 25, 2016)
    elif arg[:4] == "set(":
        setcalendar(arg)
    else:
        simpleread(arg)


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
            userinput[count] = userinput[count].encode("utf-8")
        sendstream = ' '.join(userinput)
        print('\n\n\nSUCCESS\n\n\nWill send the following term to prolog\n')
        print(sendstream)
        print(type(sendstream))
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((TCP_IP, TCP_PORT))
        s.send(bytes(sendstream).encode('utf-8'))
        data = s.recv(BUFFER_SIZE)
        print("\n\n\n\nWE GOT DATA BACK FROM PROLOG\n\n\n")
        print(data)
        s.close()
        funcparser(data)
    except sr.UnknownValueError:
        print("Assistant could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
            audio = r.listen(source)
    try:
        googleaudio = r.recognize_google(audio)
        # if googleaudio == 'hey assistant' or googleaudio == 'his system' or googleaudio == 'hey system' or googleaudio == 'his assistant' or googleaudio == 'assistance' or googleaudio == 'assistant':
        if googleaudio != "fuck you":
            print("\n\n\nSUCCESS! \n\n\nThis is assistant. How can I be of service?")
            actions()
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY", show_all=True)`
        # instead of `r.recognize_google(audio, show_all=True)`
    except sr.UnknownValueError:
        print("Assistant could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))