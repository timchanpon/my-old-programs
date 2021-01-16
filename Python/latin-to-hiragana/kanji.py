from dict import dict


def kanji(x):
	klmt = ''.join(x)
	words = []

	while ' ' in klmt:
		idx = klmt.index(' ')
		kata = change(klmt[0:idx])
		words.append(kata)
		idx += 1
		klmt = klmt[idx:]
	kata = change(klmt)
	words.append(kata)

	klmt = ''.join(words)
	return print(klmt)


def change(z):
	kata = z
	if kata in dict:
		kata = kata.replace(kata, dict[kata])

	return kata.strip()
