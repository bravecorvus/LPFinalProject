from pocketsphinx import LiveSpeech
# from pyswip import Prolog

speech = LiveSpeech(lm=False, keyphrase='backward', kws_threshold=1e+20)
for phrase in speech:
    print(phrase.segments(detailed=True))
# prolog = Prolog()
# prolog.assertz("father(michael,john)")



# prolog.assertz("father(michael,gina)")
# list(prolog.query("father(michael,X)"))
# [{'X': 'john'}, {'X': 'gina'}]
# for soln in prolog.query("father(X,Y)"):
#      print soln["X"], "is the father of", soln["Y"]    