def parser(binaryNumber):
    if(binaryNumber.count('.')==1):
        indexDot = binaryNumber.index(".")
        exp = indexDot
        mantisa = binaryNumber.replace(".","")
        decimal=0

        for index, value in enumerate(mantisa):
            decimal += int(value)*(2**(-index-1))

        decimal *= 2**exp

        print(f"Binario: {binaryNumber}")
        print(f"Decimal: {decimal}")

    else:
        decimal = int(binaryNumber, 2)

        print(f"Binario: {binaryNumber}")
        print(f"Decimal: {decimal}")

def main():
    print("Escriba el binario")
    binary = input()
    
    machineNumber(binary)
    
    
main()