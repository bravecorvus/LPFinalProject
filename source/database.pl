

greeting_db([
	hello, 
	hi, 
	hey,
	yo
	]).
goodbye_db([
	bye, 
	goodbye, 
	farewell, 
	byebye,
	'bye bye'
	]).
feelings_db([
	'how are you',
	'how are you feeling'
	]).

get_event_db([
	'what is my next calender event',
	'what is my next calendar event',
	'what is my next event',
	'get my next calender event',
	'get my next calendar event',
	'get my next event',
	'next event',
	'next calender event',
	'what is on the calender next',
	'what is on the calendar next',
	'what is on the schedule'
	]).

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

reply_db(feelings, [
	"I'm good, thank you",
	"I am feeling good",
	"Good, and you?,",
	"Better than yesterday",
	"Good, thanks for asking",
	"I'm fine",
	"Ask me something better"
	]).

reply_db(next_event,
	"get(next, event)").

reply_db(unknown,
	"I'm sorry, I could not find what you where asking for").

responses(get_event, ['get(next, calendar, event)']).
responses(set_event, ['set(next, calendar, event)']).
responses(my_name, ['My name is the Personal Assistant']).