

greeting_db([hello, hi, hey]).


thanks(['thank you', 'thanks', 'appreciated']).

reply_db(greeting, [
	'Hello!', 
	'Hi!', 
	'Welcome!', 
	'Nice to meet you'
	]).
	

responses(get_event, ['get(next, calendar, event)']).
responses(set_event, ['set(next, calendar, event)']).
responses(my_name, ['My name is the Personal Assistant']).