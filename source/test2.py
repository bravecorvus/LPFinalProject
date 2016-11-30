from pyswip import *
from random import choice
p=Prolog()
p.consult("dictionary.pl")
solutions = list(p.query("template(X),solution(X)"))
print(solutions)
