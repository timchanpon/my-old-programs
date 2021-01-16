import math

def v0_h(x):
	x[1] = x[3] = 0
	x = [float(x) for x in x]

	g = 9.8
	ud = x[0]
	mud = ud * -1
	v0 = x[2]
	h = x[4]
	xv = v0**2 + ud*2*g*h
	v = math.sqrt(xv) * ud
	t = (ud**2*math.sqrt(xv) + mud*v0) / g

	y = [v, t]
	return y

#0:ud 1:v 2:v0 3:t 4:h
