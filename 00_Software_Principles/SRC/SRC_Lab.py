# For example let create a simple project with using SRC principle:

# UI Logic (user_interface.py)
class UserInterface:
    def get_user_input(self):
        return input("Enter your name: ")

    def display_greeting(self, greeting):
        print(greeting)

# Business Logic (greeting_generator.py)
class GreetingGenerator:
    def generate_greeting(self, name):
        return f"Hello, {name}! Welcome to our system."

# Main Application (app.py)
from user_interface import UserInterface
from greeting_generator import GreetingGenerator

def main():
    user_interface = UserInterface()
    name = user_interface.get_user_input()

    greeting_generator = GreetingGenerator()
    greeting = greeting_generator.generate_greeting(name)

    user_interface.display_greeting(greeting)

if __name__ == "__main__":
    main()

# In this example, the UserInterface class handles user input and display, while the GreetingGenerator class is responsible for generating the greeting message. This separation of concerns adheres to SRP by keeping UI logic separate from business logic.

# W.I.P