:- [networker, database].
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
% choose a random response
% using the cut to not backtrack through the
% established is_function()
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

% input is an idle response
gen_reply(Q, A):-
	writeln("testing idle responses..."),
	is_idle(Q), !,
	reply_db(idle, List),
	random_member(A, List).

% input is a goodbye
gen_reply(Q, A):-
	writeln(Q),
	writeln("testing feelings..."),
	is_feeling(Q), !,
	reply_db(feelings, List),
	random_member(A, List).

% input is requesting next calendar event
gen_reply(Q, A):-
	writeln("testing known questions1... "),
	is_get_calevent(Q), !,
	reply_db(next_event, A).

% input is requesting set calendar event
gen_reply(Q, A):-
	writeln("testing known questions2... "),
	atomic_list_concat(E, " ", Q),
	is_set_calevent(E, O), !,
	atomic_list_concat(O, ",", A).

% input is a unification request
gen_reply(Q, A):-
	writeln("testing unification... "),
	is_uni(Q),
	uni_parser(Q, S),
	term_to_atom(Goal, S),
	catch(Goal, _E, fail),
	writeln(Goal),
	term_to_atom(Goal, A).

% catch-all reply
gen_reply(_, A):-
	writeln("...all tested, return nothing."),
	reply_db(unknown, A).



% helper functions____________________________________
is_uni(Q):-
    split_string(Q, " ", ",", [X|_]),
    atom_codes(W,X),
    uni_db(Z),
    member(W, Z).

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

is_set_calevent([X|Y], D):-
	set_event_db(X),
	append([create], Y, D).


is_idle(Q):-
	idle_db(List),
	member(Q, List).


%ARCHIVED functions
%testquery(Goal), call(Goal), write(Goal), nl, fail; true.
%arg(3,Goal,V),	 %Gets the (n)th argument. 
