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
