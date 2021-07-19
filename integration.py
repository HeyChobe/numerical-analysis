from math import atan, cosh, pi, sqrt, sin

def f(x):
    return 2*cosh(x)

#a: Límite inferior de la integral
#b: Límite superior de la integral
#n: Cantidad de saltos
def trapezium(a,b,n):
    h = (b-a)/n
    sumMiddle = 0
    for i in range(1, n):
        sumMiddle += f(a + i*h)
        
    return(h*(f(a)/2 + sumMiddle + f(b)/2))


#a: Límite inferior de la integral
#b: Límite superior de la integral
#n: La n multiplicada por dos, es decir, 2n
def simpson(a,b,n):
    T2n = trapezium(a,b,n)
    Tn = trapezium(a,b,n//2) 

    #Por ley general T2n = (4/3)T2n - (1/3)Tn
    print((4/3)*T2n - (1/3)*Tn)


print(trapezium(-5,5,10))
#simpson(-5,5,10)


    



    