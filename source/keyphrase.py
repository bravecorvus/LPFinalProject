from pocketsphinx import LiveSpeech
import speech_recognition as sr

def actions():
	m = sr.Recognizer()
	with sr.Microphone() as source:
	    audio = m.listen(source)
	try:
	    # for testing purposes, we're just using the default API key
	    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY", show_all=True)`
	    # instead of `r.recognize_google(audio, show_all=True)`
	    print(m.recognize_google(audio))
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
			print("This is assistant. How can I be of service?")
			actions()
	    # for testing purposes, we're just using the default API key
	    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY", show_all=True)`
	    # instead of `r.recognize_google(audio, show_all=True)`
	except sr.UnknownValueError:
	    print("Assistant could not understand audio")
	except sr.RequestError as e:
	    print("Could not request results from Google Speech Recognition service; {0}".format(e))