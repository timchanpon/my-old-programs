import codecs

with codecs.open('chat-data.txt', 'r', 'utf-8') as chat:
	text = chat.read()
	print('{}words'.format(len(text)))

i = 'y'
while i != 'n':
	a = int(input())
	b = text[a:].index('[')
	a += b
	print(a)
	print(text[a:a+25] + '\n')
	i = input()
