:- use_module(library(streampool)).

create_client(Host, Port) :-
        setup_call_catcher_cleanup(tcp_socket(Socket),
                                   tcp_connect(Socket, Host:Port),
                                   exception(_),
                                   tcp_close_socket(Socket)),
        setup_call_cleanup(tcp_open_socket(Socket, In, Out),
                           chat_to_server(In, Out),
                           close_connection(In, Out)).

chat_to_server(In, Out) :-
        read(Term),
    (   Term == end_of_file
    ->  true
    ;   format(Out, '~q .~n', [Term]),
        flush_output(Out),
        read(In, Reply),
        write(Reply),
        %format('Reply: ~q.~n', [Reply]),
        chat_to_server(In, Out)
    ).

close_connection(In, Out) :-
        close(In, [force(true)]),
        close(Out, [force(true)]).