
:- use_module(library(socket)).

server :-
  server(1025).

server(Port) :-
  udp_socket(S),
  tcp_bind(S, Port),
  repeat,
      udp_receive(Socket, Data, From, [as(atom)]),
      format('Got ~q from ~q~n', [Data, From]),
      %in_and_out_format(Codes, Result),   %external function
      fail.

send(Host, Port, Message) :-
  udp_socket(S),
  udp_send(S, Message, Host:Port, []),
  writeln("OK"),
  tcp_close_socket(S).