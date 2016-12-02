import speech_recognition as sr

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

# recognize speech using Sphinx
try:
    print("Assistant registered the phrase " + r.recognize_sphinx(audio))
except sr.UnknownValueError:
    print("Assistant could not understand audio")
except sr.RequestError as e:
    # print("Sphinx error; {0}".format(e))
    print("\n")