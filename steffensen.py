from math import cos,sin

def f(x):
    return 1+pow(sin(x),2)

def hat(p0,p1,p2):
    return p0 - (pow(p1-p0,2)/(p2-2*p1+p0))


def steffensen(p0,TOL,nMax):

    p0Hat = 0
    p1Hat = 0
    p1=0
    p2=0

    print("{0:} \t {1:} \t\t\t {2:} \t\t\t {3:} \t\t\t {4:} \t\t\t {5:}".format("i","p0","p1","p2","Hat","Error"))

    for i in range(0,nMax):
        p1=f(p0)
        p2=f(p1)
        p1Hat = hat(p0,p1,p2)

        print("{0:d} \t {1:.15f} \t {2:.15f} \t {3:.15f} \t {4:.15f} \t {5:.15f}".format(i,p0,p1,p2,p1Hat,abs(p1Hat-p0Hat)))

        if(abs(p1Hat-p0Hat)<TOL):
            break

        p0=p1Hat
        p0Hat=p1Hat


steffensen(1.5,10**-9,1000)