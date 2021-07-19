from math import cos, sin

R = 0.08205
T = 273.15
B = -1.16583607818894
r = 0.0542253936905836
zhi = -1.25100322759761 * 0.001
v0 = 0.08205*273.15/200

def f(x):
    return (R*T + (B/x) + (r/x**2) + (zhi/x**3))/200

def f1(x):
    return (-(B/x**2) - (2*r/x**3) + (zhi*3/x**4))/200

def newton(p0, TOL, Nmax):
    p = 0
    for i in range(0,Nmax):
        p = p0 - f(p0)/f1(p0)
        print("{0:d} \t {1:.15f} \t {2:.15f} \t {3:.5e}".format(i,p0,p,abs(p-p0)))
        if (abs(p-p0)<TOL):
            break
        p0=p

newton(v0,10**-9,20)
