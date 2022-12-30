"""
import random for generating random numbers
"""
import random


MAX_NUM_GUESSES = 5
PLAYER_GUESSES = 0


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
    """
    Requests player input and returns it, if it is an integer
    Displays invalid data message if not an integer
    """
    try:
        player_guess_input = int(input("Please choose a number between 1 and 100:"))
        return player_guess_input
    except ValueError:
        print("Invalid data: Your guess must be a number")
        return 0


def validate_range(player_guess_to_validate):
    """
    Check that player guess is within required range
    """
    if player_guess_to_validate < 1 or player_guess_to_validate > 100:
        print("Number must be between 1 and 100")
        return False
    else:
        return True


def check_guess(player_guess_to_check):
    """
    Check player guess against computer guess and display message to the user
    about whether their next guess should be higher or lower
    """
    if player_guess_to_check < target_number:
        print("Unlucky! The correct answer is Higher")
    elif player_guess_to_check > target_number:
        print("Unlucky! The correct answer is Lower")
    else:
        print("Congratulations, you win!")


welcome_message()

target_number = random.randrange(1, 100)

while PLAYER_GUESSES < MAX_NUM_GUESSES:
    player_guess = get_player_guess()
    GUESS_IN_RANGE = validate_range(player_guess)
    if GUESS_IN_RANGE is True:
        PLAYER_GUESSES = PLAYER_GUESSES + 1
        check_guess(player_guess)
