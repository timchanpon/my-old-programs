def v_v0(x):
	x[3] = x[4] = 0
	x = [float(x) for x in x]

	g = 9.8
	ud = x[0]
	mud = ud * -1
	v = x[1]
	v0 = x[2]
	t = (v*ud + v0*mud) / g
	h = v0*t + ud*g*t**2/2

	y = [t, h]
	return y

#0:ud 1:v 2:v0 3:t 4:h
