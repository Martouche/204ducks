## Math
## File description:
## By Bilel Bouricha
##

import sys
from math import factorial, sqrt, exp, floor
from datetime import datetime, timedelta

def GetTime(t):
    m = int(t / 60)
    s = t - (m * 60)
    if (s < 10):
        print(" {:.0f}m 0{:.0f}s".format(m, s))
    else:
        print(" {:.0f}m {:.0f}s".format(m, s))

def help():
    print("USAGE\n\t./204ducks a\n\nDESCRIPTION\n\ta\tconstant")

def average_time(a):
    res = (3 * ( a + 2)) / 8
    min = floor(res)
    sec = (res - min) * 60

    print("Average return time: {}m {:.0f}s".format(min, sec))

def average(a):
    res = (3 * ( a + 2)) / 8
    return (res)

def variance(a):
    calc = (7 / 16) * (3 * a + 2) - (average(a)* average(a))
    return sqrt(calc)

def error(a):
     if (a < 0 or a > 2.5):
        print("a is constant between 0 and 2.5")
        exit(84)

def calcul(a, t):
	calc = (1/2) * exp(-4 * t) * (exp(t) - 1)**2 * (2 * (exp(t) + 1)**2 - a * (2 * exp(t) + 1))
	return calc

def get_timer(step, a):
	t = 0
	res = 0
	while 1:
		res = calcul(a, t / 60)
		if (res >= step):
			return t
		t += 0.01

def get_pourc(step, a):
	t = 0
	res = 0
	while 1:
		res = calcul(a, t)
		if (t >= step):
			return res
		t += 0.01

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "-h":
        help()
    if len(sys.argv) != 2:
        exit(84)
    a = float(sys.argv[1])
    error(a)
    average_time(a)
    print("Standard deviation: {0:.3f}".format(variance(a)))
    print("Time after which 50% of the ducks are back:", end="")
    GetTime(get_timer(0.50, a))
    print("Time after which 99% of the ducks are back:", end="")
    GetTime(get_timer(0.99, a))
    print("Percentage of ducks back after 1 minute: {0:.1f}%".format(get_pourc(1, a) * 100 ))
    print("Percentage of ducks back after 2 minutes: {0:.1f}%".format(get_pourc(2, a) * 100))


main()
