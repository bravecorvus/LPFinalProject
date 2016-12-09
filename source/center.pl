:- use_module(library(socket)).

% Start the server in one instance of Prolog:
%  ?- server(1025).
% Start the client in another instance of Prolog:
%  ?- client(localhost:1025).

dynamic(append1/3).

server :-
  server(1025).

server(PortNumber) :-
  setup_call_cleanup(tcp_socket(S), (true; fail), tcp_close_socket(S)),
  tcp_bind(S, PortNumber),
  tcp_listen(S, 5),
  server_loop(S).

server_loop(S) :-
% S, S1=sockets, From= Client IP
  tcp_accept(S, S1, From),
  format('receiving traffic from: ~q~n', [From]),
  setup_call_cleanup(tcp_open_socket(S1, In, Out), 
    server_operation(In, Out),
    (writeln('closing...'),
    close(In),
    close(Out))), !,
  server_loop(S).

server_operation(In, Out) :-
  \+at_end_of_stream(In),
  read_pending_input(In, Codes, []),   %RECEIVING INPUT HERE
  converter(Codes, Result),
  format(Out, "~s", [Result]),
  flush_output(Out),
  server_operation(In, Out).

server_operation(_In, _Out).

converter(Codes, Result):-
  string_to_list(QueryS, Codes),
  atom_string(Query, QueryS),
  term_to_atom(X, Query),
  call(X),
  arg(3,X,V),	 %Gets the (ArgNum)th argument. 
  term_to_atom(V, ResultB),
  atom_string(ResultB, ResultA),
  string_to_list(ResultA, Result).

%Example program to be queried
append1([], L, L).
append1([X|Y], L2, [X|L3]):-
  append(Y, L2, L3).