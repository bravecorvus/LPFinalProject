%Database for the Personal Assistant project. 
%All of these functors are dependent on unification from main.pl

%INPUT DATABASE____________________________________________________
greeting_db([
	hello, 
	hi, 
	hey,
	yo,
	'hello there',
	greetings,
	greeting
	]).
goodbye_db([
	bye, 
	goodbye, 
	farewell, 
	byebye,
	'bye bye',
	'see you later'
	]).
feelings_db([
	'how are you',
	'how are you feeling',
	'whats up',
	'what is up'
	]).

get_event_db([
	'what is my next calender event',
	'whats my next calender event',
	'whats my next calendar event',
	"what's my next calender event",
	"what's my next calendar event",
	'whats my next event',
	"what's my next event",
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

set_event_db(set).
set_event_db(create).

event_db([
	to, new, set]).


thanks(['thank you', 'thanks', 'appreciated']).

idle_db([
	'good',
	'fine',
	'alright',
	'cool',
	'nice',
	'okay',
	'im good',
	'i am good',
	'i am okay',
	'i am fine',
	'i am okay',
	'it could be better',
	'bad',
	'pretty bad',
	'perfect',
	'could be better'
	]).

uni_db([
	append,
	member,
	append1
	]).


% RESPONSE DATABASE_______________________________________________
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
	"I'm good...",
	"Better than yesterday",
	"Good, thanks for asking",
	"I'm fine",
	"Ask me something better"
	]).

reply_db(next_event,
	"get(next, calender, event)").

reply_db(unknown,
	"I have not learned that yet...").

reply_db(idle, [
	"Ask me something else",
	"Mhm...",
	"..."
	]).
