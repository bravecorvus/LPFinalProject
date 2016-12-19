% Code based on Clocksin chapter 09 - "Using Prolog Grammar Rules"
% Designed to be a subpart of the Personal Assistant project

   sentence(Z):-  question_p(X),  noun_p(Y),  append(X,Y,Z).
   
   question_p(Z):-  pronoun(X),  verb(Y),  append(X,Y,Z).
   question_p(Z):-  pronoun(Z).
   
   noun_p(Z):-  noun(Z).
   noun_p(Z):-  noun(X), noun(Y), append(X, Y, Z).
   noun_p(Z):-  adj_p(X), noun(Y), append(X, Y, Z).

   adj_p(Z):- 	det(X), adj(Y), append(X, Y, Z).
   
   pronoun([what]).
   pronoun([whats]).
   
   verb([is]).
   verb([are]).
   verb([be]).
   
   noun([event]).
   noun([calender]).
   noun([calendar]).

   det([my]).
   det([your]).
   det([yours]).

   adj([next]).
   adj([coming]).