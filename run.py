"""
import random for generating random numbers
"""
import random


class GameStatus:
    """
    Sets and displays number of guesses taken and remaining in game
    """
    def __init__(self, incorrect, correct, max_guesses):
        self.incorrect = incorrect
        self.correct = correct
        self.max_guesses = max_guesses

    def add_incorrect_guess(self):
        """
        Function to increment incorrect guesses
        """
        self.incorrect = self.incorrect + 1

    def add_correct_guess(self):
        """
        Function to set correct to true when number is guessed correctly
        """
        self.correct = True

    def display_game(self):
        """
        Function to display current game status
        """
        print("====================")
        print("Remaining Guesses")
        print("====================")

        for x in range(self.max_guesses - self.incorrect):
            print("X")

        print("====================\n")


def welcome_message():
    """
    Displays welcome message to the user
    """
    print("Welcome!")
    print("To play the game, choose a number between 1 and 100")
    print("You have 5 chances to guess the target number\n")

    inputted_player_name = input("Please enter your name:\n")
    print(f"Hi {inputted_player_name}, let's play the game!")
    return inputted_player_name


def get_player_guess():
    """
    Requests player input and returns it, if it is an integer
    Displays invalid data message if not an integer
    """
    try:
        player_guess_input = int(input("Please choose a number between 1 and 100 (or 999 to exit):\n"))
        return player_guess_input
    except ValueError:
        print("Invalid input. Your guess must be a number")
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


def validate_unique_guess(player_guess_to_validate, player_previous_guesses):
    """
    Check if the current guess is in the list of previous guesses
    """
    is_unique_guess = False
    if player_guess_to_validate in player_previous_guesses:
        print("Guess already in list of previous guesses")
        print(f"Your previous guesses were: {player_previous_guesses}")
        print("Please try again\n")
    else:
        player_previous_guesses.append(player_guess_to_validate)
        is_unique_guess = True
    return is_unique_guess


def check_guess(player_guess_to_check, check_if_number_guessed):
    """
    Check player guess against target number and display message to the user
    about whether their next guess should be higher or lower
    """
    if player_guess_to_check < target_number:
        print("Unlucky! The correct answer is Higher\n")
    elif player_guess_to_check > target_number:
        print("Unlucky! The correct answer is Lower\n")
    else:
        check_if_number_guessed = True
    return check_if_number_guessed


MAX_NUM_GUESSES = 5
player_guesses = 0
target_number_guessed = False
previous_guesses = []
target_number = random.randrange(1, 100)
game_status_display = GameStatus(player_guesses, False, MAX_NUM_GUESSES)


player_name = welcome_message()

game_status_display.display_game()

while player_guesses < MAX_NUM_GUESSES:
    if target_number_guessed is True:
        break

    player_guess = get_player_guess()

    if player_guess == 999:
        break

    GUESS_IN_RANGE = validate_range(player_guess)
    GUESS_IS_UNIQUE = validate_unique_guess(player_guess, previous_guesses)

    if GUESS_IN_RANGE is True and GUESS_IS_UNIQUE is True:
        player_guesses = player_guesses + 1

        target_number_guessed = check_guess(player_guess, target_number_guessed)

        if target_number_guessed is False:
            game_status_display.add_incorrect_guess()
        else:
            game_status_display.add_correct_guess()

        game_status_display.display_game()


print("====================")
print("===  GAME OVER!  ===")
print("====================")
if target_number_guessed is True:
    print(f"Congratulations {player_name}, you win!")
else:
    print(f"You lose {player_name}!")
print(f"The correct number was {target_number}")
