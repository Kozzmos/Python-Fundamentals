#  LAB 04 Exception Handling

# Exception handling in Python allows us to gracefully manage errors and unexpected situations that
# may arise during the execution of our code.

# Try-Except Statement:

# The try-except statement allows us to handle exceptions (errors) that occur within a block of code.
# We place the code that may raise an exception inside the try block, and we specify how to handle
# the exception(s) in the except block.

try:
    # Code that may raise an exception
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result:", result)
except ZeroDivisionError:
    # Handling the ZeroDivisionError exception
    print("Cannot divide by zero.")
except ValueError:
    # Handling the ValueError exception
    print("Invalid input. Please enter a number.")

# Finally Block:

# The finally block is used to execute code regardless of whether an exception occurred or not.
# It is commonly used for cleanup tasks such as closing files or releasing resources.

try:
    file = open("example.txt", "r")
    # Perform some operations with the file
except FileNotFoundError:
    print("File not found.")
finally:
    # Close the file in the finally block to ensure it's always executed
    file.close()  # This will execute even if an exception occurs in the try block

# Combining Try-Except-Finally:

# We can combine the try-except and finally blocks to handle exceptions and perform cleanup actions.

try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result:", result)
except ZeroDivisionError:
    print("Cannot divide by zero.")
finally:
    print("Thank you for using the program. Exiting...")

# The finally block is useful for ensuring that certain actions are always performed, regardless
# of whether an exception occurred or not.
