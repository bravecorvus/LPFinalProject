% Network part of the Personal Assistant project
:- use_module(library(socket)).

% convenience functor that chooses a default portnumber
server :-
  server(1025).

% create a socket connection that listens for incoming connections
% setup - creates the socket, fails when it fails/breaks
% server loop is the next step wich progress when connection is established
server(PortNumber) :-
  setup_call_cleanup(tcp_socket(S), (true; fail), tcp_close_socket(S)),
  tcp_bind(S, PortNumber),
  tcp_listen(S, 5),
  server_loop(S).

% server loop that accepts and closes data streams. 
% server operation is the next step to handle the inputted data
server_loop(S) :-
  tcp_accept(S, S1, From),
  writeln(From),
  setup_call_cleanup(tcp_open_socket(S1, In, Out), 
    server_operation(In, Out),
    (writeln('closing...'),
    close(In),
    close(Out))), !,
  server_loop(S).

% server operation which formats the input and output stream
% in and out format is the next step to use in main.pl
server_operation(In, Out) :-
  \+at_end_of_stream(In),
  read_pending_input(In, Codes, []),  %RECEIVING INPUT HERE
  in_and_out_format(Codes, Result),   %external function to understand input
  format(Out, "~s", [Result]),
  flush_output(Out),
  server_operation(In, Out).

server_operation(_In, _Out).