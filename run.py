"""
Start of the game function
"""
def welcome():
    print('Welcome to the text-based adventure game "QB1".')
    print("In this game you are the quarterback of the New York Giants in the Super Bowl against the Kansas City Chiefs.")
    print("Make the right decisions and win the game of the year!\n")
    user_choice_welcome()

"""
Function to let user decide between starting the game or reading the rules
"""
def user_choice_welcome():
    print("Do you want to start the game or read the rules?")
    print("1. Start the game")
    print("2. Read the rules\n")

    user_choice_welcome_input = input("Your choice (1/2): ")

    if user_choice_welcome_input == "1":
        print("Let the games begin...")
        #Add function for game start here!
    elif user_choice_welcome_input == "2":
        print("Here are the rules...")
        game_rules()
    else:
        print("Invalid input. Please choose again.")
        return user_choice_welcome()

"""
Function to display rules and let user decide if he wants do get back to menu or start game directly
"""
def game_rules():
    print("\nGame Rules:")
    print("You are the QB of your team and must make crucial decisions to win the game.")
    print("The coin toss will be your first decision and determines who gets the ball first. Then, you can decide how to play the ball.")
    print("There are different options, and randomness determines what happens. You can score points or lose the ball.")
    print("The game ends after 10 possessions you had. The one with more points wins the Super Bowl!\n")
    game_rules_navigation()

def game_rules_navigation():
    print("Do you want to start the game now or go back to the welcome menu?")
    print("1. Start the game")
    print("2. Welcome menu\n")
    user_choice_rules = input("Your choice (1/2): ")
    if user_choice_rules == "1":
        print("Let the games begin...")
    elif user_choice_rules == "2":
        welcome()
    else:
        print("Invalid input. Please choose again.")
        return game_rules_navigation()


welcome()