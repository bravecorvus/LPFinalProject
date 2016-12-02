from pocketsphinx import LiveSpeech
import speech_recognition as sr

def actions() {
	r = sr.Recognizer()
	with sr.Microphone() as source:
	    audio = r.listen(source)
	try:
	    # for testing purposes, we're just using the default API key
	    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY", show_all=True)`
	    # instead of `r.recognize_google(audio, show_all=True)`
	    print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
	except sr.UnknownValueError:
	    print("Google Speech Recognition could not understand audio")
	except sr.RequestError as e:
	    print("Could not request results from Google Speech Recognition service; {0}".format(e))	
}

r = sr.Recognizer()
with sr.Microphone() as source:
	    audio = r.listen(source)
try:
	if r.recognize_google(audio) == 'hey assistant':
		print("This is assistant. How can I be of service?")
		actions()
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY", show_all=True)`
    # instead of `r.recognize_google(audio, show_all=True)`
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))





	# print("I am Your Assitant, say something for me to assist you")
	# r = sr.Recognizer()
	# with sr.Microphone() as source:
	# 	keyphrase = r.listen(source)
	# try:
	# 	print("Assistant registered the phrase " + r.recognize_sphinx(keyphrase))
	# except sr.UnknownValueError:
	# 	print("Assistant could not understand audio")
	# except sr.RequestError as e:
	# 	# print("Sphinx error; {0}".format(e))
	# 	print("\n")