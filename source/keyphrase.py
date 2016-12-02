import speech_recognition as sr

# obtain audio from the microphone
r1 = sr.Recognizer()
r2 = sr.Recognizer()
while True:
	with sr.Microphone() as source:
	    print("I am Your Assitant, say something for me to assist you")
	    keyphrase = r1.listen(source)
	try:
		if r1.recognize_sphinx(keyphrase) == "hey assistant":
			print("Listening for commands")
			with sr.Microphone() as source:
			    command = r2.listen(source)
			try:
	            print("Assistant registered the phrase " + r2.recognize_sphinx(command))
	        except sr.UnknownValueError:
	            print("Assistant could not understand audio")
	        except sr.RequestError as m:
	            print("Sphinx error; {0}".format(m))                

	except sr.UnknownValueError:
	    print("Assistant could not understand audio")
	except sr.RequestError as e:
	    # print("Sphinx error; {0}".format(e))
	    print("\n")