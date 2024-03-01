#  LAB 01 Introduction to Python

# Basic printing code for Python

print("Hello World!")
print("\n")  # \n is used to go next line in python

# How to define a variable ?
# In Python, you don't have to clarify the type of the variable

new_variable_int = 0
new_variable_string = "Hello World!"
new_variable_float = 3.1415926
new_variable_double = 3.141592653589793
new_variable_char = "x"
new_variable_bool = True

# To print a variable we can only use the name of variable

print(new_variable_int)
print(new_variable_string)
print(new_variable_float)
print(new_variable_double)
print(new_variable_char)
print(new_variable_bool)
print("\n")

# To check the type of variable we have type() function
print(type(new_variable_int))
print(type(new_variable_string))
print(type(new_variable_float))
print(type(new_variable_double))
print(type(new_variable_char))  # When you try this code it will give String output because python process char as a string value even if it's a character
print(type(new_variable_bool))
print("\n")

# OPERATORS
# Arithmetic Operators

# In Python, we have 7 arithmetic operators. Which are Addition (+), Subtraction(-), Multiplication(*), Division(/),Modulus(%), Exponentiation(**), Floor Division(//)

# Let's use them in examples

num_1 = 5
num_2 = 3

print(num_1 + num_2)
print(num_1 - num_2)
print(num_1 * num_2)
print(num_1 / num_2)
print(num_1 % num_2)
print(num_1 ** num_2)
print(num_1 // num_2)
print("\n")

# Assignment Operators, in Python we have 8  assignment operators

# Assignment Operator (=): Assigns a value to a variable
a = 5  # Assigning the value 5 to the variable a

# Addition Assignment Operator (+=): Adds a value to the variable and assigns the result to the variable
b = 10
b += 5  # Equivalent to b = b + 5
print(b)

# Subtraction Assignment Operator (-=): Subtracts a value from the variable and assigns the result to the variable
c = 20
c -= 3  # Equivalent to c = c - 3
print(c)

# Multiplication Assignment Operator (*=): Multiplies the variable by a value and assigns the result to the variable
d = 8
d *= 2  # Equivalent to d = d * 2
print(d)

# Division Assignment Operator (/=): Divides the variable by a value and assigns the result to the variable
e = 25
e /= 5  # Equivalent to e = e / 5
print(e)

# Modulus Assignment Operator (%=): Computes the remainder of division and assigns the result to the variable
f = 17
f %= 4  # Equivalent to f = f % 4
print(f)

# Exponentiation Assignment Operator (**=): Raises the variable to the power of a value and assigns the result
g = 3
g **= 4  # Equivalent to g = g ** 4
print(g)

# Floor Division Assignment Operator (//=): Performs floor division and assigns the result to the variable
h = 27
h //= 5  # Equivalent to h = h // 5
print(h)
print("\n")

# Comparison Operators, in Python we have 6 comparison operators

# Comparison Operator (==): Checks if two values are equal
a = 5
b = 5
print(a == b)

# Not Equal Operator (!=): Checks if two values are not equal
print(a != b)

# Greater Than Operator (>): Checks if one value is greater than another
print(a > b)

# Greater Than or Equal To Operator (>=): Checks if one value is greater than or equal to another
print(a >= b)

# Less Than Operator (<): Checks if one value is less than another
print(a < b)

# Less Than or Equal To Operator (<=): Checks if one value is less than or equal to another
print(a <= b)

# Chained Comparison Operators: Combining multiple comparison operators
c = 10
print(5 < c < 15)
print("\n")

# Logical Operators, in Python we have 3 logical operators

# Logical AND Operator (and): Returns True if both operands are True
a = True
b = False
print(a and b)

# Logical OR Operator (or): Returns True if at least one operand is True
print(a or b)

# Logical NOT Operator (not):
print(not a)

# Combining Logical Operators: Complex logical expressions
x = 5
print(x > 0 and x < 10)

# Short-Circuit Evaluation: Stops evaluating expression when result is already known
y = 10
print(x > 0 or y < 0)
