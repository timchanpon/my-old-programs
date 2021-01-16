def v0_t(x):
	x[1] = x[4] = 0
	x = [float(x) for x in x]

	g = 9.8
	ud = x[0]
	mud = ud * -1
	v0 = x[2]
	t = x[3]
	v = v0 + ud*g*t
	h = v0*t + ud*g*t**2/2

	y = [v, h]
	return y

#0:ud 1:v 2:v0 3:t 4:h
