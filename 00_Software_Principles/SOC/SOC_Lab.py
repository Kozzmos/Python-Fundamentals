# For example let create a simple project with using SOC principle:

# UI Logic (user_input.py)

class UserInput:
    def get_user_input(self):
        return input("Enter your name: ")

# Business Logic (greeting.py)
class Greeting:
    def greet_user(self, name):
        return f"Hello, {name}! Welcome to our system."

# Main Application (app.py)
from user_input import UserInput
from greeting import Greeting

def main():
    user_input = UserInput()
    name = user_input.get_user_input()

    greeting = Greeting()
    message = greeting.greet_user(name)

    print(message)

if __name__ == "__main__":
    main()

# In this example, the UI logic (capturing user input) is separated from the business logic (generating a greeting message). The UserInput class handles user input, while the Greeting class handles generating the greeting message. This separation allows for easier maintenance and testing of each concern independently.

# WIP

