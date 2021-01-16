i = 1
while i == 1:
	question = ['投げ上げなら「up」を、投げ下げなら「down」を入力して下さい。', '\n(求めたいデータには「x」を入力して下さい。)\n速度を入力して下さい。', '\n初速度を入力して下さい。', '\n時間を入力して下さい。', '\n高さを入力して下さい。']

	ii = 0
	data = []
	while ii < 5:
		print(question[ii])
		data.append(input())
		ii += 1
	if data[0] == 'up' and data.count('x') < 3:
		data[0] = -1
	elif data[0] == 'down' and data.count('x') < 3:
		data[0] = 1
	elif data.count('x') > 2:
		print('\n「x」は2つ以内で入力して下さい。\n')
		continue
	else:
		print('\nもう一度入力して下さい。\n')
		continue

	if data[3] == 'x' and data[4] == 'x':
		from v_v0 import v_v0
		y = v_v0(data)
		t = str(y[0])
		h = str(y[1])
		print('\n時間は「'+ t +'」で、\n高さは「'+ h +'」です。')

	elif data[2] == 'x' and data[4] == 'x':
		from v_t import v_t
		y = v_t(data)
		v0 = str(y[0])
		h = str(y[1])
		print('\n初速度は「'+ v0 +'」で、\n高さは「'+ h +'」です。')

	elif data[2] == 'x' and data[3] == 'x':
		from v_h import v_h
		y = v_h(data)
		v0 = str(y[0])
		t = str(y[1])
		print('\n時間は「'+ v0 +'」で、\n高さは「'+ t +'」です。')

	elif data[1] == 'x' and data[4] == 'x':
		from v0_t import v0_t
		y = v0_t(data)
		v = str(y[0])
		h = str(y[1])
		print('\n速度は「'+ v +'」で、\n高さは「'+ h +'」です。')

	elif data[1] == 'x' and data[3] == 'x':
		from v0_h import v0_h
		y = v0_h(data)
		v = str(y[0])
		t = str(y[1])
		print('\n速度は「'+ v +'」で、\n時間は「'+ t +'」です。')

	elif data[1] == 'x' and data[2] == 'x':
		from t_h import t_h
		y = t_h(data)
		v0 = str(y[0])
		v = str(y[1])
		print('\n速度は「'+ v +'」で、\n初速度は「'+ v0 +'」です。')

	else:
		print('\nもう一度入力して下さい。\n')
		continue

	print('\n続ける場合は「y」を、続けない場合は「n」を入力して下さい。')
	c = input()
	if c == 'y' or c == 'Y':
		print('\n-------------------------\n')
		continue
	else:
		print('\nThank you for using!!\n')
		break

#0:ud 1:v 2:v0 3:t 4:h
