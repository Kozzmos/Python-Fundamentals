#  LAB 03 Loops

# Loops:

# For Loop: The for loop allows us to iterate over a sequence (e.g., list, tuple, string) and execute
# a block of code for each item in the sequence.
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# While Loop: The while loop allows us to execute a block of code as long as a condition is true.
count = 0
while count < 5:
    print("Count:", count)
    count += 1

# Loop Control Statements:

# Break Statement: The break statement allows us to exit the loop prematurely based on a certain condition.
for i in range(10):
    if i == 5:
        break
    print(i)

# Continue Statement: The continue statement allows us to skip the rest of the loop's code for the current
# iteration and move on to the next iteration.
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

# Nested Loops: Loops can be nested within each other, allowing for more complex iteration patterns.
for i in range(3):
    for j in range(3):
        print(i, j)

# These control flow structures provide powerful mechanisms for writing dynamic and flexible code,
# allowing programs to make decisions and repeat tasks as needed.