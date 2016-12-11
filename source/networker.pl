:- use_module(library(socket)).

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
  in_and_out_format(Codes, Result),   %external function to understand input
  format(Out, "~s", [Result]),
  flush_output(Out),
  server_operation(In, Out).

server_operation(_In, _Out).
