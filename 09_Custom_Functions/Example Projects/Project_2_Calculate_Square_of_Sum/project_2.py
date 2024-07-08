def getnum():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    num3 = int(input("Enter third number: "))
    numf = num1 + num2 + num3
    return numf

def calc(numf: int):
    final = numf ** 2
    return final

def main():
    print(calc(getnum()))

main()
