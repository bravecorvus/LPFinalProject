:- use_module(library(socket)).


create_server(Port) :-
        tcp_socket(Socket),
        tcp_bind(Socket, Port),
        tcp_listen(Socket, 5),
        tcp_open_socket(Socket, AcceptFd, _),
    dispatch(AcceptFd).

dispatch(AcceptFd) :-
        tcp_accept(AcceptFd, Socket, Peer),
        thread_create(process_client(Socket, Peer), _,
                      [ detached(true)
                      ]),
        dispatch(AcceptFd).

process_client(Socket, _Peer) :-
        setup_call_cleanup(tcp_open_socket(Socket, In, Out),
                           handle_service(In, Out),
                           close_connection(In, Out)).

close_connection(In, Out) :-
        close(In, [force(true)]),
        close(Out, [force(true)]).

handle_service(In, Out) :-
    read(In, Int),
    writeln(Int),
    (   Int == end_of_file
    ->  true
    ;   
        call_test(Int,Term),
        format(Out, 'seen(~q).~n', [Term]),
        flush_output(Out),
        handle_service(In, Out)
    ).

call_test(test,Term):-Term = 'really test'.
call_test(validate(teste),Term):-
    String = "validate(test)",
    string_to_list(String,List),
    read_from_chars(List,Stringf),
    writeln(Stringf), 
    Term = 'foo'.