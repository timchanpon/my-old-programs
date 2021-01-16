import codecs, pickle


'''
dict area
'''
'''
wordsDict = {
	'saja, aja':0,
	'yang, yg':0,
	'kalau, kalo, klo':0,
	'memang, emng':0,
	'terus, trus':0,
	'ngopi':0,
	'alhamdulillah':0
}'''

with open('words-dict.txt', 'rb') as dict:
	wordsDict = pickle.load(dict)


'''
def area
'''
# editing data to make the sorting's precision high
def edit_data(pro):
	print('..def edit_data')

	replaceList = [',', '.', '?', '!', '*', '[', ']', ':', '/', '😆', '😂', '🤣', '😁', '\'', '\"']

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

# to separate words and add '@'
def edit_wordPro(wordPro):
	print('..def edit_wordPro')
	if ',' in wordPro:
		wordProList = list()
		i = 0
		while ',' in wordPro[i:]:
			end = wordPro[i:].index(',')
			end += i
			pro = '@' + wordPro[i:end] + '@'
			wordProList.append(pro)
			i = end+2
		pro = '@' + wordPro[i:] + '@'
		wordProList.append(pro)
		wordPro = wordProList
	else:
		wordPro = '@' + wordPro + '@'

	print('finish')
	return wordPro


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
	data = edit_data(data)

print('complete\n')

# make wordsTuple
print('make wordsTuple')
wordsKeyList = list()
for key in wordsDict:
	wordsKeyList.append(key)
wordsTuple = tuple(wordsKeyList)

print('complete\n')

# make and fill wordList
print('make and fill wordList')
wordsList = list()
for wordPro in wordsDict:
	wordPro = edit_wordPro(wordPro)
	if type(wordPro) == list:
		wordsList.append('Head')
		for proA in wordPro:
			wordsList.append(proA)
		wordsList.append('End')
	else:
		wordsList.append(wordPro)

print('complete\n')

# calculate
print('calculate')
i = 0
count = 0
while count < len(wordsTuple):
	proB = wordsList[i]
	if proB == 'Head':
		end = wordsList[i:].index('End')
		ii = 0
		while ii < end-1:
			ii += 1
			proC = wordsList[i+ii]
			#print(proC)
			#print(data.count(proC))
			wordsDict[wordsTuple[count]] += data.count(proC)
		i += end+1

	else:
		#print(proB)
		#print(data.count(proB))
		wordsDict[wordsTuple[count]] += data.count(proB)
		i += 1

	count += 1

print('complete\n')

# print
print('print\n')
for i in wordsDict.items():
	print('{} : {}times'.format(i[0], i[1]))

print('\ncomplete')
print('\n__End__')
