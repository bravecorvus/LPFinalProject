% Code based on Clocksin chapter 09 - "Using Prolog Grammar Rules"
% Designed to be a subpart of the Personal Assistant project

sentence(S) --> sentence(_X, S).

sentence(X, sentence(QP, VP)) --> question_phrase(X, QP), verb_phrase(X, VP).

question_phrase(X, question_phrase(D, N)) --> pronoun(X, D), verb(X, N).

verb_phrase(X, verb_phrase(V)) --> verb(X, V).
verb_phrase(X, verb_phrase(V, NP)) --> verb(X, V), question_phrase(_Y, NP).


pronoun(_, pronoun(what)) --> [what].
verb(singular, verv(is)) --> [is].

is_noun(banana, singular).
is_noun(apple, singular).
is_noun(boy, singular).

noun(singular, noun(man)) --> [man].
noun(plural, noun(man)) --> [men].
noun(singular, noun(child)) --> [child].
noun(plural, noun(child)) --> [children].

noun(S, noun(N)) --> [N], {is_noun(N, S)}.
noun(plural, noun(RootN)) -->
    [N],
    {   atom_chars(N, PlName),
        append(SingName, [s], PlName),
        atom_chars(RootN, SingName),
        is_noun(RootN, singular)}.


verb(singular, verb(eats)) --> [eats].
verb(plural, verb(eat)) --> [eat].
verb(singular, verb(sings)) --> [sings].
verb(plural, verb(sing)) --> [sing].




sentence(s(X, Y, Z)) --> question_phrase(X), determiner(Y), noun_phrase(Z).

noun_phrase(np(X)) --> adjective(X), noun(X).

belonging_phrase(belong(my)) --> [my].

determiner(dtmnr([my])) --> [my].
adjective(adj(next)) --> [next].
noun(noun(calender)) --> [calender].
noun(noun(event)) --> [event].
noun(noun(calender, event)) --> [calender, event].


question(X) -->  [what, is],  belonging_phrase(X), abstract_noun(Y).   
