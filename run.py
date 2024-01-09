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
        print("Here are the rules!")
        #Add function for game start here!
    else:
        print("Invalid input. Please choose again.")
        return user_choice_welcome()

welcome()