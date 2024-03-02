#  LAB 02 Control Flow

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

# Control flow in Python allows us to execute certain blocks of code conditionally or iteratively,
# based on the evaluation of expressions or the occurrence of events.

# Conditional Statements:

# If Statement: The if statement allows us to execute a block of code if a condition is true.
age = 20
if age >= 18:
    print("You are an adult.")

# If-Else Statement: The if-else statement allows us to execute one block of code if the condition is true,
# and another block of code if the condition is false.
age = 15
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# If-Elif-Else Statement: The if-elif-else statement allows us to check multiple conditions and execute
# different blocks of code based on the evaluation of these conditions.
temperature = 25
if temperature > 30:
    print("It's hot outside!")
elif temperature > 20:
    print("It's warm outside.")
else:
    print("It's cold outside.")