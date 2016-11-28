from pocketsphinx import LiveSpeech
from pyswip import Prolog, Functor, Variable, Query
prolog = Prolog()
userinput = ""
print('Welcome to SWI-Prolog (Multi-threaded, 64 bits, Version 7.2.3)\nCopyright (c) 1990-2015 University of Amsterdam, VU Amsterdam\nSWI-Prolog comes with ABSOLUTELY NO WARRANTY. This is free software,\nand you are welcome to redistribute it under certain conditions.\nPlease visit http://www.swi-prolog.org for details")\n\n For help, use ?- help(Topic). or ?- apropos(Word).')
prolog.consult("dictionary.pl")
while True:
    userinput = input("?- ")
    if userinput == "exit()":
        break
    else:
        list(prolog.query(userinput))

# Primary Action File. Does all the work between listening for human input, and passing along the text to Prolog
# Once Prolog returns the appropriate function, Python will execute it and return the state back to suspend until the keyword is invoked again