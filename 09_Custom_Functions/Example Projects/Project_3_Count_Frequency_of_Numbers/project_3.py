numbers = [4, 8, 9, 4, 2, 5, 6, 4, 6, 8, 4, 1, 8, 4, 7, 2, 1, 8, 9, 4, 5, 4]

def amount_inlist(numbers: list):
    amount = {}
    counter = 0
    for i in numbers:
        for j in numbers:
            if i == j:
                counter += 1
        amount[i] = counter
        counter = 0
    return amount

print(amount_inlist(numbers))
