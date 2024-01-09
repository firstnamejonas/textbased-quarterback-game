import time
import random

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
Functions to display rules and let user decide if he wants do get back to menu or start game directly (navigation function)
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

"""
Function to start the game. The game starts with the first decission: the cointoss!
"""
def start_game_with_cointoss():
    print("Welcome to the Super Bowl, the most prestigious sporting event of the year!")
    print("--- New York Giants : Kansas City Chiefs ---")
    print("It's time for the game to begin, but who will get the ball first and the chance to score the first points?")
    print("It's your turn!\n")
    print("Do you want to choose Heads or Tails?")
    print("1. Heads")
    print("2. Tails")

    user_choice_cointoss = input("Your choice (1/2): ")

    num=random.randint(1,2)

    if num==1:
        result="1"
    elif num==2:
        result="2"
    if user_choice_cointoss == result:
        print("Congrats! Your first win, you get the ball to start the game!\n")
        giants_possession()
    else:
        print("Aw...You've lost the cointoss, but this means nothing!\n")
        chiefs_posession()

"""
Function when chiefs are in posession. USER HAS NO CONTROL!
"""
def chiefs_posession():
    print("The Chiefs are in posession...\n")
    if random.random() < 0.4:
        print("The Chiefs score a TD!")
        print("Now it's your turn! Go get some points...\n")
        # Funktion für +7 Punkte einfügen 
        giants_possession()
    elif random.random() < 0.4:
        print("Your defense held and forced a turnover on downs!")
        print("Now it's your turn! Go get some points...\n")
        giants_possession()
    else:
        print("Your defense has achieved a turnover!")
        print("Now it's your turn! Go get some points...\n")
        giants_possession()

welcome()