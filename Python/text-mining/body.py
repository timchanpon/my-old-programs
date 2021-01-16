import codecs
from def_box import remover, calc, edit_lower, del_word, write_result, word_toplist


with codecs.open('chat-data.txt', 'r', 'utf-8') as chat:
	text = chat.read()
	text = text.replace('\n', '＠')
	text = text.replace(' ', '＠')
	'''
	amountCalc = int(input('How many elements do you want to calculate?\n'))
	amountIndex = text[amountCalc:].index('[')
	amountCalc += amountIndex

	text = remover(text[:amountCalc])
	'''
	text = remover(text)


word = dict()
i = 0
print('\nSortation of words is started.\n')
nama = 'Sorted'
while i < len(text):
	calc(i, len(text), nama)
	wordEndIndex = text[i:].index('＠')
	wordEnd = i + wordEndIndex
	wordPro = edit_lower(text[i:wordEnd])
	if wordPro in word:
		word[wordPro] += 1
	else:
		word[wordPro] = 1

	i = wordEnd + 1

print('100% Sortation complete.\n')


del_word(word)

keyList = list()
for i in word:
	keyList.append(i)

valueList = list()
for i in word.values():
	valueList.append(i)

write_result(keyList, valueList)


amountResult = int(input('\nHow many results do you want? (in range {})\n'.format(len(keyList))))
print('\n')

wordTopList = word_toplist(keyList, valueList, amountResult)

i = num = 0
while i < amountResult*2:
	newKey = wordTopList[i]
	newValue = wordTopList[i+1]
	print('{}. '.format(num+1) + newKey + '({}times)'.format(newValue))
	i += 2
	num += 1


print('\n__End__')
