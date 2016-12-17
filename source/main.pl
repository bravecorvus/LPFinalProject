:- [networker, appender, database].
:- use_module(library(random)).

% Compile this program to include functions in networker and any other file:
% start server with
% ?- start(1025). or ?- start.

start:-
	server.
start(X):-
	server(X).

% Reads in input from connection and generates
% a reply based on the content
in_and_out_format(Codes, Result):-
	string_to_list(QueryS, Codes),
	atom_string(Query, QueryS),
	gen_reply(Query, ResultB),
	atom_string(ResultB, ResultA),
	string_to_list(ResultA, Result).

% input is a unification request
gen_reply(Q, A):-
	is_uni(Q, A), !.

% input is a greeting
gen_reply(Q, A):-
	is_greeting(Q), !,
	reply_db(greeting, List),
	writeln(List),
	random_member(A, List).



is_uni(Q, A):-
	writeln("testing unification... "),
	term_to_atom(Goal, Q),
	catch(Goal, _E, fail),
	writeln(Goal),
	term_to_atom(Goal, A).

is_greeting(Q):-
	writeln("testing greeting... "),
	greeting_db(List),
	member(Q, List).



%ARCHIVED functions
%testquery(Goal), call(Goal), write(Goal), nl, fail; true.
%arg(3,Goal,V),	 %Gets the (n)th argument. 
