lst = [12, 11, 19, 2, 99]
lst_1 = []
lst_2 = []

def duo(sayi: int):
    for i in range(len(lst)):
        if sayi % 2 == 0:
            return "even"
        else:
            return "odd"

def append(result: str, num: int):
    if result == "even":
        lst_1.append(num * 2)
    else:
        lst_2.append(num * 3)

def main():
    for i in lst:
        result = duo(i)
        append(result, i)
    print(lst_1)
    print(lst_2)

main()
