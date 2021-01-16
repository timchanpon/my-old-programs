import codecs, pickle
from def_box import calc


'''
def area
'''
# editing data to make the sorting's precision high
def edit_data(pro):
	print('..def edit_data')

	replaceList = [',', '.', '?', '!', '*', '[', ']', ':', '/', '😆', '😂', '🤣', '😁', '\u200e', '\'', '\"']

	for i in range(0, 10):
		replaceList.append(str(i))

	for i in replaceList:
		if i in pro:
			pro = pro.replace(i, '@')

	pro = list(pro)
	for i, new in enumerate(pro):
		new = new.lower()
		pro[i] = new

	print('finish')
	return ''.join(pro)


'''
body area
'''
# open chat-data and edit it
print('open chat-data and edit it')
with codecs.open('chat-data.txt', 'r', 'utf-8') as chat:
	data = chat.read()
	if '@' in data:
		data = data.replace('@', '＠')
	data = data.replace('\n', '@')
	data = data.replace(' ', '@')
	data = edit_data(data[0:50051])

print('complete\n')

# sort words and add it to wordsDict
print('sort words')
wordsDict = dict()
i = 0
while i < len(data)-1:
	i += 1
	calc(i, len(data), 'Sorted')
	wordEnd = data[i:].index('@')
	wordEnd += i
	word = data[i:wordEnd]
	if word in wordsDict:
		i = wordEnd
		continue
	else:
		wordsDict[word] = 0
	i = wordEnd

if '' in wordsDict:
	del wordsDict['']

print('100% complete\n')

# write out wordsDict to 'words-dict.txt'
print('write out wordsDict to \'words-dict.py\'')
with open('words-dict.txt', 'wb') as dict:
	pickle.dump(wordsDict, dict)

print('complete\n')
print('__End__')
