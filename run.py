import random


max_num_guesses = 5
player_guesses = 0


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
        player_guess = int(input("Please choose a number between 1 and 100:"))
        return player_guess
    except ValueError:
        print("Invalid data: Your guess must be a number")
        return 0


def check_guess(player_guess):
    """
    Check player guess against computer guess and display message to the user
    about whether their next guess should be higher or lower
    """
    if player_guess < target_number:
        print("Unlucky! The correct answer is Higher")
    elif player_guess > target_number:
        print("Unlucky! The correct answer is Lower")
    else:
        print("Congratulations, you win!")


welcome_message()

target_number = random.randrange(1, 100)

while player_guesses < max_num_guesses:
    player_guess = get_player_guess()
    player_guesses = player_guesses + 1
    check_guess(player_guess)

