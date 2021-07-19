from math import cos

def f(x):
    return cos(x)-x

def secante(p0,p1,TOL,nMax):
    p = 0

    print("{0:} \t {1:} \t\t\t {2:} \t\t\t {3:} \t\t\t {4:}".format("i","p0","p1","p","Error"))

    for i in range(0,nMax):
        p = p1 - (f(p1)*(p1-p0))/(f(p1)-f(p0))

        print("{0:d} \t {1:.15f} \t {2:.15f} \t {3:.15f} \t {4:.15f}".format(i,p0,p1,p,abs(p-p0)))

        if(abs(p - p1)< TOL):
            break

        p0=p1
        p1=p

#Suelo tener una tolerancia muy grande
secante(0.4,0.5,10**-16,10000)