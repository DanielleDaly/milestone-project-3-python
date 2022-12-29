import random


def welcome_message():
    """
    Displays welcome message to the user
    """
    print("Welcome!")
    print("Please choose a number between 1 and 100")
    print("You have 5 chances to guess the correct answer\n")

    player_name = input("Please enter your name:\n")
    print(f"Hi {player_name}, ready to play the game?")


welcome_message()

computer_guess = random.randrange(1, 100)
player_guess = int(input("Please choose a number between 1 and 100:"))
while computer_guess != player_guess:
    if player_guess < computer_guess:
        print("Unlucky! The correct answer is Higher")
        player_guess = int(input("Please choose another number:"))
    elif player_guess > computer_guess:
        print("Unlucky! The correct answer is Lower")
        player_guess = int(input("Please choose another number:"))
    else:
        break
print("Congratulations, you win!")
