append1([], L, L).
append1([X|Y], L2, [X|L3]):-
  append(Y, L2, L3).