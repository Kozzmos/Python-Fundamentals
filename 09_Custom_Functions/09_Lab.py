import string

# Declaring a function
# def function_name():
#     business logic

# Call a function
# function_name()

def greet():
    print("hi")

greet()

def calc(x: int, y: int):
    """
    Adds two numbers and prints the result.
    :param x: First integer
    :param y: Second integer
    :return: None
    """
    print(f"{x} + {y} = {x + y}")

calc(2, 5)

def alpha(x: int):
    """
    Checks if a number is prime and prints the result.
    :param x: Integer to check
    :return: None
    """
    counter = 0
    for i in range(1, x+1):
        if x % i == 0:
            counter += 1
    if counter == 2:
        print("asal")
    else:
        print("asal değil")

alpha(7)

def mail(name: string):
    """
    Generates an email address from a name.
    :param name: Full name
    :return: None
    """
    x = name.lower().split(" ")
    print(f"{x[0]}.{x[-1]}@bilgeadam.com")

mail("akif eren ertugrul")

def fac(x: int):
    """
    Calculates the factorial of a number and prints the result.
    :param x: Integer to calculate factorial for
    :return: None
    """
    num = 1
    for i in range(1, x+1):
        num *= i
    print(num)

fac(3)

def login(name: string, password: string, user_list: list):
    """
    Authenticates a user against a list of users.
    :param name: Username
    :param password: User password
    :param user_list: List of tuples containing usernames and passwords
    :return: None
    """
    for i, j in user_list:
        if i == name and j == password:
            print("welcome")
            break
    else:
        print("invalid user or password")

users = [("beast", "123"), ("bear", "234"), ("savage", "789")]
x = input("Name: ")
y = input("Pass: ")
login(x, y, users)
