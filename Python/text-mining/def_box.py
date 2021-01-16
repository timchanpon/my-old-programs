import codecs


def remover(text):
	print('\nWait a moment.. removing unneeded words from chat-data.\n')
	text = list(text)
	text = [i for i in text if not i == ',' and not i == '.' and not i == '😆' and not i == '😂' and not i == '?' and not i == '!' and not i == '*' and not i == '😁' and not i == '🤣' and not i == '\"' and not i == '\'']
	print('Removing complete.')

	print('\nRemoving meta-data from chat-data, is started.\n')
	i = 0
	len = text.count('[')
	nama = 'Removed'
	while '[' in text:
		calc(i, len, nama)
		dataHead = text.index('[')
		dataEnd = text.index(']')
		namaEndIndex = text[dataEnd:].index(':')
		namaEnd = dataEnd + namaEndIndex
		del text[dataHead:namaEnd+2]
		i += 1

	print('100% Removing complete.\n')
	return ''.join(text)


def calc(i, len, nama):
	progress = i/len * 100

	return print('{}% ({}/{}) {}'.format(int(progress),i ,len, nama))


def edit_lower(wordPro):
	wordPro = list(wordPro)
	for i, new in enumerate(wordPro):
		new = wordPro[i]
		new = new.lower()
		wordPro[i] = new

	return ''.join(wordPro)


def del_word(word):
	if '' in word:
		del word['']
	'''
	if 'soki' in word:
		del word['soki']
	if 'ghina' in word:
		del word['ghina']
	'''


def write_result(keyList, valueList):
	wordList = list()
	i = 0
	while i < len(keyList):
		wordList.append(keyList[i])
		wordList.append(' ({}times)'.format(valueList[i]))
		wordList.append('\n')
		i += 1

	wordList = ''.join(wordList)
	with codecs.open('word-result.txt', 'w', 'utf-8') as result:
		result.write(wordList)

	return print('\nWriting out the word-dict data to word-result.txt, success.\n')


def word_toplist(keyList, valueList, amountResult):
	wordTopList = list()
	for i in range(amountResult):
		maxIndex = valueList.index(max(valueList))
		maxKey = keyList[maxIndex]
		maxValue = valueList[maxIndex]
		wordTopList.append(maxKey)
		wordTopList.append(maxValue)
		del keyList[maxIndex]
		del valueList[maxIndex]

	return wordTopList
