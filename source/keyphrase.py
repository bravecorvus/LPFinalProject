from pocketsphinx import LiveSpeech
import speech_recognition as sr

# obtain audio from the microphone
while True:
	speech = LiveSpeech(lm=False, keyphrase='hey assistant', kws_threshold=1e+20)
	for phrase in speech:
	    print(phrase.segments(detailed=True))
	    r = sr.Recognizer()
		with sr.Microphone() as source:
		    print("I am Your Assitant, say something for me to assist you")
		    keyphrase = r.listen(source)
		try:
			print("Assistant registered the phrase " + r.recognize_sphinx(audio))
		except sr.UnknownValueError:
		    print("Assistant could not understand audio")
		except sr.RequestError as e:
		    # print("Sphinx error; {0}".format(e))
		    print("\n")