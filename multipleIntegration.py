from math import e, pi, sin, cos
from sympy import Symbol, Function, E
from sympy.polys.rings import xring

x = Symbol('x')
y = Symbol('y')

f = pow(e,y/x)


def double_integral_rectangular(a,b,c,d,m,n):

    h = (b-a)/n
    k = (d-c)/m

    sumPairK = 0
    sumPairH = 0
    sumNotPairK = 0
    sumNotPairH = 0

    for i in range(1,(m//2)+1):
        sumNotPairK += f.subs(y,c + (2*i - 1)*k)
        #sumNotPairK += f(x,c + (2*i - 1)*k)

    for i in range(1,(m//2)):
        sumPairK += f.subs(y,c + 2*i*k)
        #sumPairK += f(x,c + 2*i*k)

    g = (k/3)*(f.subs(y,c) + 4*sumNotPairK + 2*sumPairK + f.subs(y,d))

    for i in range(1,(n//2)+1):
        sumNotPairH += g.subs(x, a + (2*i - 1)*h)

    for i in range(1,(n//2)):
        sumPairH += g.subs(x,a + 2*i*h)

    print((h/3)*(g.subs(x,a) + 4*sumNotPairH + 2*sumPairH + g.subs(x,b)))

double_integral_rectangular(1.3,1.5,-0.1,0.1,4,2)