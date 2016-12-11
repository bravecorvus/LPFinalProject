:- [networker].
:- [appender].

% Compile this program to include functions in network and any other file:
% start server with
% ?- server(1025). or ?- server.

in_and_out_format(Codes, Result):-
  string_to_list(QueryS, Codes),
  atom_string(Query, QueryS),
  term_to_atom(Goal, Query),
  call(Goal),
  writeln(Goal),
  %arg(3,Goal,V),	 %Gets the (n)th argument. 
  term_to_atom(Goal, ResultB),
  atom_string(ResultB, ResultA),
  string_to_list(ResultA, Result).

%testquery(Goal), call(Goal), write(Goal), nl, fail; true.