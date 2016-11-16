from pocketsphinx import LiveSpeech
from pyswip import Prolog

# Primary Action File. Does all the work between listening for human input, and passing along the text to Prolog
# Once Prolog returns the appropriate function, Python will execute it and return the state back to suspend until the keyword is invoked again