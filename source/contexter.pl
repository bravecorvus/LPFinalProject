% Code based on Clocksin chapter 09 - "Using Prolog Grammar Rules"
% Designed to be a subpart of the Personal Assistant project


sentence --> sentence(_X).

sentence(X) --> question_phrase(X), objective_phrase(X).
sentence(X) --> 

question_phrase(X) --> pronoun(X), aux_verb(X).

objective_phrase(X) --> adjective(X).
objective_phrase(X) --> verb(X), noun_phrase(_Y).

adjective(1st) --> [next].


determiner(_) --> [my].

noun(singular) --> [apple].
noun(plural) --> [apples].
noun(singular) --> [man].
noun(plural) --> [men].
noun(singular) --> [boy].
noun(plural) --> [boys].

verb(singular) --> [eats].
verb(plural) --> [eat].
verb(singular) --> [sings].
verb(plural) --> [sing].
