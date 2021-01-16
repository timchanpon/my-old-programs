import math

def v_h(x):
	x[2] = x[3] = 0
	x = [float(x) for x in x]

	g = 9.8
	ud = x[0]
	mud = ud * -1
	v = x[1]
	h = x[4]
	xv0 = mud*2*g*h + v**2
	v0 = math.sqrt(xv0)
	t = (ud*v + mud*math.sqrt(xv0)) / g

	y = [v0, t]
	return y

#0:ud 1:v 2:v0 3:t 4:h
