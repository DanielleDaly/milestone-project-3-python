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


def get_player_guess():
    try:
        player_guess = int(input("Please choose a number between 1 and 100:"))
    except ValueError:
        print("Invalid data: Your guess must be a number")
        player_guess = int(input("Please choose a number between 1 and 100:"))
    return player_guess


def check_guess(player_guess):
    """
    Check player guess against computer guess and display message to the user
    about whether their next guess should be higher or lower
    """
    while computer_guess != player_guess:
        if player_guess < computer_guess:
            print("Unlucky! The correct answer is Higher")
        elif player_guess > computer_guess:
            print("Unlucky! The correct answer is Lower")
        else:
            break
    print("Congratulations, you win!")


welcome_message()

computer_guess = random.randrange(1, 100)

player_guess = get_player_guess()


# if player_guess > 100:
# # raise ValueError("Invalid data: you must choose a number less than 100")
