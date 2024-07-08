from pprint import pprint
import random

# Sign-In/Sign-Up System
users = {
    "1": {
        "Username": "beast",
        "Password": "123"
    },
    "2": {
        "Username": "savage",
        "Password": "123"
    }
}
counter = 3

def counterupdater():
    global counter
    counter += 1
    return counter

def signup(username: str, password: str, counter: int):
    users[str(counter)] = {
        "Username": username,
        "Password": password
    }
    counter = counterupdater()
    print("Sign up successful!")

def signin(username: str, password: str) -> bool:
    for user_data in users.values():
        if user_data["Username"] == username and user_data["Password"] == password:
            print("Sign in successful!")
            return True
    print("Invalid username or password")
    return False

def signupcheck(username: str) -> bool:
    for user_data in users.values():
        if user_data["Username"] == username:
            print("Username is already taken")
            return True
    return False

def main():
    global counter
    print("Manual Guide\n" "=============\n" "Sign In\n" "Sign Up\n" "List\n" "Exit\n")
    while True:
        process = input("Type a Process: ").lower()

        if process == "exit":
            print("Application has been closed!")
            break
        elif process == "sign in":
            username = input("Username: ")
            password = input("Password: ")
            signin(username, password)
        elif process == "sign up":
            username = input("Username: ")
            password = input("Password: ")
            if not signupcheck(username):
                signup(username, password, counter)
        elif process == "list":
            pprint(users)
        else:
            print("Please type a valid process")

main()

# Betting Game
users = {
    "1": {
        "Username": "beast",
        "Password": "123",
        "safe": 1200
    },
    "2": {
        "Username": "savage",
        "Password": "123",
        "safe": 2000
    }
}
minbet = 100
bots = ["John", "Rick", "Akif"]

def login(username: str, password: str) -> dict:
    is_active = False
    user_id = ""
    for i in range(1, len(users)+1):
        if users.get(str(i)).get("Username") == username and users.get(str(i)).get("Password") == password:
            is_active = True
            user_id = str(i)
            print(f"Sign in successful!")
            break
        else:
            print("Invalid username or password")
    if is_active:
        return users.get(user_id)

def update_safe(user: dict, gains: int) -> None:
    user.update({
        "safe": user.get("safe") + gains
    })

def is_betvalid(bet: int, safe: int) -> bool:
    return 50 < bet < safe

def assign_default_player(bots: list) -> str:
    return random.choice(bots)

def roll_dice() -> int:
    return random.randint(2, 12)

def dailybonus() -> int:
    daily = random.randint(1000, 2000)
    print(f"You won a free {daily} chip, don't forget to log in again tomorrow")
    return daily

def main():
    auth_user = login(
        input("Username: "),
        input("Password: ")
    )
    if auth_user:
        daily = dailybonus()
        update_safe(auth_user, daily)
        print(f"Current Safe {auth_user.get('safe')}")
        while True:
            if auth_user.get("safe") >= minbet:
                bet = int(input("Please make a bet: "))
                if is_betvalid(bet, auth_user.get('safe')):
                    opponent = assign_default_player(bots)
                    print(f"Your opponent is {opponent}")

                    my_dice = roll_dice()
                    opponent_dice = roll_dice()

                    print(f"Your Dice {my_dice}\nYour Opponent's Dice {opponent_dice}")
                    if my_dice > opponent_dice:
                        update_safe(auth_user, bet)
                        print(f"You Won!!! \nYour Current Safe Balance: {auth_user.get('safe')}")
                    elif my_dice == opponent_dice:
                        print("Your dice are tied, there is no winner this round.")
                    else:
                        update_safe(auth_user, -bet)
                        print(f"You Lost... \nYour Current Safe Balance: {auth_user.get('safe')}")
                else:
                    print("Please make a valid bet")
            else:
                print("Your safe is under the minimum table bet...!\nDo you want to buy more chips?")
                break

main()
