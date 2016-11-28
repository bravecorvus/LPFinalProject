# 'philosopher.py' a basic chatbot learning system
# using pyswip which interfaces python and swi-prolog

from pyswip import *
from random import choice

# start a Prolog interpreter instance
p=Prolog()

# load the ontology specification
p.consult("c.pl")

# construct look up tables of common facts 
properties = list(p.query("property(X,Y)"))
categories = list(p.query("parent(X,Y)"))
cousins = list(p.query("cousin(X,Y)"))

# prepare for saving of new inferences
new_prolog_code = open('d.pl','w')
new_facts = []


def say_property_fact():
    """chooses a random fact about one of a category's
    properties and states it"""
    selected_fact=choice(properties)
    return selected_fact['Y']+'s '+selected_fact['X']

def say_category_fact():
    """chooses a random fact about category membership
    and states it"""
    selected_fact=choice(categories)
    return 'a '+selected_fact['Y']+' is a kind of '+selected_fact['X']

def ask_cousin_property():
    """hypothesises that cousins share properties
    and asks for confirmation, saving new code if yes"""
    cousin_pair = choice(cousins)
    props = list(p.query("property(X,"+cousin_pair['Y']+")"))
    possible_property  = choice(props)
    print 'does a '+cousin_pair['X']+' '+possible_property['X']+'?'
    a= raw_input('y or n')
    if a == 'y':
        new_facts.append('property('+possible_property['X']+','+cousin_pair['X']+').\n')
    else:
        return
        
# uncheck to say some facts as a test
#print say_property_fact() 
#print say_category_fact()

# does a training run and saves new inferences

response = ''

while response == '':
    ask_cousin_property()
    response = raw_input('quit ?')

new_set_of_facts = list(set(new_facts))

for x in new_set_of_facts:
    new_prolog_code.write(x)

new_prolog_code.close()

print "thank you, 'philosopher' has learned something new"