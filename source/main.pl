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

% input is a greeting
gen_reply(Q, A):-
	writeln("testing greeting... "),
	is_greeting(Q), !,
	reply_db(greeting, List),
	random_member(A, List).

% input is a goodbye
gen_reply(Q, A):-
	writeln("testing goodbye..."),
	is_goodbye(Q), !,
	reply_db(goodbye, List),
	random_member(A, List).

% input is a goodbye
gen_reply(Q, A):-
	writeln("testing feelings..."),
	is_feeling(Q), !,
	reply_db(feelings, List),
	random_member(A, List).

% input is requesting next calendar event
gen_reply(Q, A):-
	writeln("testing known questions1... "),
	is_get_calevent(Q), !,
	reply_db(next_event, A).

% input is a unification request
gen_reply(Q, A):-
	writeln("testing unification... "),
	is_uni(Q, A), !.

% catch-all reply
gen_reply(_, A):-
	writeln("...all tested, return nothing."),
	reply_db(unknown, A).


is_uni(Q, A):-
	term_to_atom(Goal, Q),
	catch(Goal, _E, fail),
	writeln(Goal),
	term_to_atom(Goal, A).

is_greeting(Q):-
	greeting_db(List),
	member(Q, List).

is_goodbye(Q):-
	goodbye_db(List),
	member(Q, List).

is_feeling(Q):-
	feelings_db(List),
	member(Q, List).

is_get_calevent(Q):-
	get_event_db(List),
	member(Q, List).


%ARCHIVED functions
%testquery(Goal), call(Goal), write(Goal), nl, fail; true.
%arg(3,Goal,V),	 %Gets the (n)th argument. 
