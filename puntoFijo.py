from math import cos, sqrt, sin

'''
g: función continua con un único punto fijo
p0: valor inicial aproximado del punto fijo
TOL: precisión deseada
nMax: iteraciones
'''

#Se ingresa la derivada para calcular K
def fixedPointD(g, p0, TOL, nMax, g2):
    print("i\t p0\t\t\t p\t\t\t |p-p0| \t K")
    for i in range(0,nMax):
        p=g(p0)
        print("{0:d} \t {1:.15f} \t {2:.15f} \t {3:.5e} \t {4:.5e}".format(i,p0,p,abs(p-p0),g2(p)))
        if abs(p-p0)<TOL:
            break
        p0=p


#Calculando K sin derivada
def fixedPoint(g, p0, TOL, nMax):
    print("i\t p0\t\t\t p\t\t\t |p-p0| \t K")
    error = 0.00001

    for i in range(0,nMax):
        p=g(p0)
        lastError = error
        error = abs(p-p0)
        print("{0:d} \t {1:.15f} \t {2:.15f} \t {3:.5e} \t {4:.15f}".format(i,p0,p,error,abs(error/lastError)))
        if abs(p-p0)<TOL:
            break
        p0=p

# fixedPointD(lambda x: sqrt(x+1), 0, 10**-10, 1000, lambda x: (1/2)*(x+1)**(-1/2))
fixedPoint(lambda x: 1 + pow(sin(x),2), 1.5, 10**-9, 1000)