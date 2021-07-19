def floatPoint(mantisa):
    normalizedMantisa = 0

    for index, value in enumerate(mantisa):
        normalizedMantisa += int(value)*pow(2,-index-1)

    return normalizedMantisa

def machineNumber(sign, exp, mantisa):
    expDecimal = int(exp,2)
    expSize = len(exp)
    expMax=""
    expMin=""
    next= bin(int(mantisa,2)+1).replace("0b", "")
    nextMantisa = floatPoint(next)
    last= bin(int(mantisa,2)-1).replace("0b", "")
    lastMantisa = floatPoint(last)
    mantisaDecimal = floatPoint(mantisa)

    for i in range(expSize):
        expMax+="1"
        expMin+="0"

    expMaxDecimal = int(expMax,2) + 1
    sesgo = expMaxDecimal/2

    lastDecimal= pow(-1, int(sign)) * pow(2,expDecimal - sesgo) * lastMantisa
    decimal = pow(-1, int(sign)) * pow(2,expDecimal - sesgo) * mantisaDecimal
    nextDecimal= pow(-1, int(sign)) * pow(2,expDecimal - sesgo) * nextMantisa
    print(f"\nSigno: {sign} | Exponente: {exp} | Mantisa: {mantisa}")
    print(f"(-1)^{sign} x 2^({expDecimal} -{sesgo}) x {mantisa}")
    print(f"Decimal: {decimal}")
    print(f"Siguiente número:\n\tBinario: {next}\n\tDecimal: {nextDecimal}")
    print(f"Anterior número:\n\tBinario: {last}\n\tDecimal: {lastDecimal}")

def main():
    print("Escriba el signo")
    sign = input()
    print("Escriba el exponente")
    exp = input()
    print("Escriba la mantisa")
    mantisa = input()
    machineNumber(sign, exp, mantisa)
    
    
main()