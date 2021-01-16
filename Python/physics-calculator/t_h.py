def t_h(x):
	x[1] = x[2] = 0
	x = [float(x) for x in x]

	g = 9.8
	ud = x[0]
	mud = ud * -1
	t = x[3]
	h = x[4]
	v0 = mud*g*t/2 + h/t
	v = v0 + ud*g*t

	y = [v0, v]
	return y

#0:ud 1:v 2:v0 3:t 4:h
