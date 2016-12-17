

greeting_db([hello, hi, hey]).
goodbye_db([bye, goodbye, farewell, byebye]).

thanks(['thank you', 'thanks', 'appreciated']).

reply_db(greeting, [
	'Hello!', 
	'Hi!', 
	'Welcome!', 
	'Nice to meet you'
	]).

reply_db(goodbye, [
	'Goodbye',
	'Bye!',
	'Have a nice day!',
	'Byebye'
	]).

reply_db(unknown,
	"I'm sorry, I could not find what you where asking for").

responses(get_event, ['get(next, calendar, event)']).
responses(set_event, ['set(next, calendar, event)']).
responses(my_name, ['My name is the Personal Assistant']).