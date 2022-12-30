"""
import random for generating random numbers
"""
import random


class GameStatus:
    """
    Sets and displays number of guesses taken and remaining in game
    """
    def __init__(self, incorrect, correct, max):
        self.incorrect = incorrect
        self.correct = correct
        self.max = max

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
        print("********************")
        print("Remaining Guesses")

        for x in range(self.max - self.incorrect):
            print("X")

        print("********************")


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


def check_guess(player_guess_to_check, check_if_number_guessed):
    """
    Check player guess against computer guess and display message to the user
    about whether their next guess should be higher or lower
    """
    if player_guess_to_check < target_number:
        print("Unlucky! The correct answer is Higher")
    elif player_guess_to_check > target_number:
        print("Unlucky! The correct answer is Lower")
    else:
        check_if_number_guessed = True
    return check_if_number_guessed


MAX_NUM_GUESSES = 5
PLAYER_GUESSES = 0
target_number_guessed = False
target_number = random.randrange(1, 100)
game_status_display = GameStatus(PLAYER_GUESSES, False, MAX_NUM_GUESSES)


welcome_message()

while PLAYER_GUESSES < MAX_NUM_GUESSES:
    if target_number_guessed is True:
        break
    player_guess = get_player_guess()
    GUESS_IN_RANGE = validate_range(player_guess)
    if GUESS_IN_RANGE is True:
        PLAYER_GUESSES = PLAYER_GUESSES + 1
        target_number_guessed = check_guess(player_guess, target_number_guessed)
        if target_number_guessed is False:
            game_status_display.add_incorrect_guess()
        else:
            game_status_display.add_correct_guess()
        game_status_display.display_game()


print("*** GAME OVER ***")
if target_number_guessed is True:
    print("Congratulations, you win!")
else:
    print("You lose!")
print(f"The correct number was {target_number}")