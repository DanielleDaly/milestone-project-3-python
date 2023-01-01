"""
Use import random for generating random number for the target number
in the game
"""
import random


class GameStatus:
    """
    Maintains the number of incorrect guesses made
    Maintains True/False for whether a correct guess has been made
    Displays remaining guesses in the game
    """
    def __init__(self, incorrect, correct, max_guesses):
        """
        Set default values
        """
        self.incorrect = incorrect
        self.correct = correct
        self.max_guesses = max_guesses

    def add_incorrect_guess(self):
        """
        Increments incorrect guesses
        """
        self.incorrect = self.incorrect + 1

    def add_correct_guess(self):
        """
        Sets correct to True when number is guessed correctly
        """
        self.correct = True

    def display_game(self):
        """
        Display remaining guesses
        """
        print("====================")
        print("Remaining Guesses")
        print("====================")

        # Loop through number of remaining guesses
        for x in range(self.max_guesses - self.incorrect):
            print("X")

        print("====================\n")


def welcome_message():
    """
    Displays welcome message to the player
    Takes the players name as input
    Display welcome to the player with their inputted name
    Returns it for Win/Lose messaging
    """
    print("======================================================")
    print("Welcome!")
    print("To play the game, choose a number between 1 and 100")
    print("You have 5 chances to guess the target number")
    print("======================================================\n")

    inputted_player_name = input("Please enter your name:\n")
    print(f"Hi {inputted_player_name}, let's play the game!\n")
    return inputted_player_name


def get_player_guess():
    """
    Requests player input and returns it, if it is an integer
    Displays invalid data message if not an integer
    """
    try:
        print("Please choose a number between 1 and 100 (or 999 to exit)")
        player_guess_input = int(input("Enter number:\n"))
        return player_guess_input
    except ValueError:
        print("Invalid input. Your guess must be a whole number\n")
        return 422


def validate_range(player_guess_to_validate):
    """
    Check that player guess is within the required range
    """
    if player_guess_to_validate < 1 or player_guess_to_validate > 100:
        # Only show the error message if the number is not 422
        # 422 is the number as the Invalid Data return when getting the player's guess
        if player_guess_to_validate != 422:
            print("The number you entered was outside the range 1 to 100\n")

        return False
    else:
        return True


def validate_unique_guess(player_guess_to_validate, player_previous_guesses):
    """
    Check if the current guess is in the list of previous guesses
    Return True if number is unique
    Add number to list of previous guesses if unique
    """
    is_unique_guess = False
    if player_guess_to_validate in player_previous_guesses:
        print("Guess already in list of previous guesses")
        print(f"Your previous guesses were: {player_previous_guesses}")
        print("Please try again\n")
    else:
        if player_guess_to_validate != 422:
            player_previous_guesses.append(player_guess_to_validate)
            is_unique_guess = True
    return is_unique_guess


def check_guess(player_guess_to_check, check_if_number_guessed):
    """
    Check player guess against target number and display message to the user
    The message states whether the target number is higher or lower
    If the correct number is guessed sets check_if_number_guessed to True
    """
    if player_guess_to_check < target_number:
        print("Unlucky! The correct answer is Higher\n")
    elif player_guess_to_check > target_number:
        print("Unlucky! The correct answer is Lower\n")
    else:
        check_if_number_guessed = True
    return check_if_number_guessed


# Declare variables
MAX_NUM_GUESSES = 5
player_guesses = 0
target_guessed = False
previous_guesses = []
# Get random number as target number for game
target_number = random.randrange(1, 100)
# Create instance of GameStatus
game_status_display = GameStatus(player_guesses, False, MAX_NUM_GUESSES)

# Call welcome_message function and set player_name to returned value
player_name = welcome_message()

# Show remaining guesses at the start of the game
game_status_display.display_game()

# Loop until MAX_NUM_GUESSES reached
while player_guesses < MAX_NUM_GUESSES:
    # Breaks loop if target number is guessed
    if target_guessed is True:
        break

    # Get player guess
    player_guess = get_player_guess()

    # Breaks out of loop if player inputs "quit" number
    if player_guess == 999:
        break

    # Validate guess
    GUESS_IN_RANGE = validate_range(player_guess)
    GUESS_IS_UNIQUE = validate_unique_guess(player_guess, previous_guesses)

    # If the guess is valid
    if GUESS_IN_RANGE is True and GUESS_IS_UNIQUE is True:
        # Increment player guesses
        player_guesses = player_guesses + 1

        # Check if player has guessed the correct number
        target_guessed = check_guess(player_guess, target_guessed)

        # Handle result of check for correct guess
        if target_guessed is False:
            game_status_display.add_incorrect_guess()
        else:
            game_status_display.add_correct_guess()

        # Display remaining guesses
        game_status_display.display_game()


# End of Game
print("====================")
print("===  GAME OVER!  ===")
print("====================")
# Display appropriate Win/Lose message
if target_guessed is True:
    print(f"Congratulations {player_name}, you win!")
else:
    print(f"Oh no! Sorry {player_name}, you have lost the game!")
# Display the target number
print(f"The correct number was {target_number}")
