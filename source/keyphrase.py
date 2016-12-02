import speech_recognition as sr

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("I am Your Assitant, say something for me to assist you")
    keyphrase = r.listen(source)

# recognize speech using Sphinx
try:
    if r.recognize_sphinx(keyphrase) == "hey assistant":
        try:
            command = r.listen(source)
            print(print("Assistant registered the phrase " + r.recognize_sphinx(command)))
        except sr.UnknownValueError:
            print("Assistant could not understand audio")
        except sr.RequestError as e:
            print("Sphinx error; {0}".format(e))                

except sr.UnknownValueError:
    print("Assistant could not understand audio")
except sr.RequestError as e:
    # print("Sphinx error; {0}".format(e))
    print("\n")