from chars import aiu, a, i, u, e, o, sml
from kanji import kanji


ipt = input()
klmt = []
len = len(ipt)
cnt = 0


while cnt < len:
	x = 2
	wn = ipt[cnt].lower()
	if len-cnt != 1:
		tu = ipt[cnt+1].lower()

	if wn in aiu:
		str = aiu[wn]
		x = 1
	elif wn == tu and tu not in aiu and tu != 'n':
		str = 'っ'
		x = 1

	elif tu == 'a':
		str = a[wn]
	elif tu == 'i':
		str = i[wn]
	elif tu == 'u':
		str = u[wn]
	elif tu == 'e':
		str = e[wn]
	elif tu == 'o':
		str = o[wn]
	elif wn == 'n' == tu or tu == 'g':
		str = 'ん'

	elif wn in a and tu == 'y' and len-cnt != 1:
		tu = ipt[cnt+2].lower()
		x = 3
		if wn == 'l':
			str = sml[tu]
		else:
			str = sml[wn] + sml[tu]

	else:
		str = wn
		x = 1

	klmt.append(str)
	cnt += x


kanji(klmt)
