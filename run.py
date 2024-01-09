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
        time.sleep(2)
        start_game_with_cointoss()
    elif user_choice_welcome_input == "2":
        print("Here are the rules...")
        time.sleep(2)
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
    time.sleep(2)
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

"""
Function when the Giants (The User) is in possession of the ball with random starting position and yard line. 
"""
def giants_possession():
    yard_line = random.randint(1, 50)
    starting_position = random.choice(["own", "opponents"])

    print(f"You start at your {starting_position} {yard_line} Yard line!")
    giants_posession_choose_play()

"""
Function for user to decide what play to be played.
"""
def giants_posession_choose_play():
    print("\nWhich play do you choose?")
    print("1. Long Pass to WR")
    print("2. Short Pass to WR")
    print("3. Short Pass to TE")

    qb_choice = input("Your choice (1/2/3): ")
    
    if qb_choice == "1":
        if random.random() < 0.5:
            print("Congrats! You've scored a TOUCHDOWN!")
            print("Take a breather while the Chiefs are on offense...\n")
            # Funktion für +7 Punkte einfügen 
            chiefs_posession()
        elif random.random() < 0.5:
            print("Completion! You achieved a new first down and move further down the field!")
            # Funktion für weiteren Ballbesitz weiter unten des Feldes
        elif random.random() < 0.5:
            print("Incomplete pass! The Chiefs defense has blocked your pass!")
            # Funktion für 2,3,4 & 10 - STOP wenn nach 4&10 immernoch nicht weiter gekommen ist
        else:
            print("OH NOOOO! You're pass has been intercepted! Now the Chiefs have the ball!")
            print("Keep ypur head up! Take a breather and come back stronger after their posession!")
            chiefs_posession()
    elif qb_choice == "2":
        if random.random() < 0.3:
            print("Congrats! You've scored a TOUCHDOWN!")
            print("Take a breather while the Chiefs are on offense...\n")
            # Funktion für +7 Punkte einfügen 
            chiefs_posession()
        elif random.random() < 0.9:
            print("Completion! You achieved a new first down and move further down the field!")
            # Funktion für weiteren Ballbesitz weiter unten des Feldes
        elif random.random() < 0.3:
            print("Incomplete pass! The Chiefs defense has blocked your pass!")
            # Funktion für 2,3,4 & 10 - STOP wenn nach 4&10 immernoch nicht weiter gekommen ist
        else:
            print("OH NOOOO! You're pass has been intercepted! Now the Chiefs have the ball!")
            print("Keep ypur head up! Take a breather and come back stronger after their posession!")
            chiefs_posession()
    elif qb_choice == "3":
        if random.random() < 0.3:
            print("Congrats! You've scored a TOUCHDOWN!")
            print("Take a breather while the Chiefs are on offense...\n")
            # Funktion für +7 Punkte einfügen 
            chiefs_posession()
        elif random.random() < 0.9:
            print("Completion! You achieved a new first down and move further down the field!")
            # Funktion für weiteren Ballbesitz weiter unten des Feldes
        elif random.random() < 0.3:
            print("Incomplete pass! The Chiefs defense has blocked your pass!")
            # Funktion für 2,3,4 & 10 - STOP wenn nach 4&10 immernoch nicht weiter gekommen ist
        else:
            print("OH NOOOO! You're pass has been intercepted! Now the Chiefs have the ball!")
            print("Keep your head up! Take a breather and come back stronger after their posession!")
            chiefs_posession()
    else:
        print("Invalid play. Please choose again.")
        return giants_posession_choose_play()

welcome()