from math import cos, ceil, log, sqrt, asin, pi, e, sin

# Nuestra función en forma f(x) - x = 0

def f(x):
    return 0.5 + 0.5*pow(e,-x/(2*pi))*sin(x) - 0.75

def bisectionPLUS(f, a, b, TOL):
    # Calculando el número de iteraciones
    n = ceil(log((b-a)/TOL, 2))
    last = 0
    flag = False

    print("i" + "\t " +  "an" +  "\t\t\t " +  "bn" +  "\t\t\t " +  "pn" +  "\t\t\t " + "f(p)" + "\t\t\t " +  "ERROR" + "\t ") 

    for i in range(0, n):

        p = (a+b)/2
        if (abs(((p-last)/p))<TOL):
            flag = False
        else:
            flag = True
        
        print("{0:d} \t {1:.15f} \t {2:.15f} \t {3:.15f} \t {4:.15f} \t {5:.15f} \t {6:}".format(i,a,b,p,f(p),(p-last)/p,flag))


        if(f(a)*f(p) < 0):
            b = p
            last = p
        else:
            a = p
            last = p

bisectionPLUS(f, 0, 2.1, 0.2)



