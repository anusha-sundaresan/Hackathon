import random

# Program to play number guessing game with the user

def get_user_input():
    while True:
        try:
            user_input = int(input("Enter a number: "))
            return user_input
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    random_number = random.randint(1, 100)
    user_number = get_user_input()

    while user_number != random_number:
        if user_number < random_number:
            print("Too low!")
        else:
            print("Too high!")

        user_number = get_user_input()

    print("Congratulations! You guessed the number correctly.")