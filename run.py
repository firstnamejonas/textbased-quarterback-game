import os
import time
import random
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)


def clear():
    """
    Clear function to clean-up the terminal so things don't get messy.
    """
    os.system("cls" if os.name == "nt" else "clear")


def welcome():
    """
    Start of the game function
    """
    clear()
    print(f'{Fore.WHITE}Welcome to the text-based adventure game "QB1".')
    print("In this game you are the quarterback of the New York Giants ")
    print("in the Super Bowl against the Kansas City Chiefs.")
    print("Make the right decisions and win the game of the year!\n")
    user_choice_welcome()


def user_choice_welcome():
    """
    Function to let user decide between starting the game or reading the rules
    """
    while True:
        print("Do you want to start the game or read the rules?")
        print(f"{Fore.YELLOW}1. {Fore.WHITE}Start the game")
        print(f"{Fore.YELLOW}2. {Fore.WHITE}Read the rules\n")

        user_choice_welcome_input = input(
            f"{Fore.YELLOW}Your choice (1/2):\n"
        )
        clear()

        if user_choice_welcome_input == "1":
            print(f"{Fore.WHITE}Let the games begin...")
            time.sleep(2)
            start_game()
            break
        elif user_choice_welcome_input == "2":
            print(f"{Fore.WHITE}Here are the rules...")
            time.sleep(2)
            game_rules()
            break
        else:
            print(
                f"{Fore.RED}{user_choice_welcome_input} "
                "is an invalid input. Please choose again."
            )


def game_rules():
    """
    Functions to display rules and let user decide if he wants
    do get back to menu or start game directly (navigation function)
    """
    clear()
    print("Game Rules:")
    print("You as the Quarterback make crucial decisions for your team.")
    print("From the cointoss to offensive play calling - YOU DECIDE!")
    print("There are different options (numbers to choose) for each play.")
    print("Randomness decides the outcome, from Touchdowns to Interceptions.")
    print("NOTE: If you score a TD you'll automatically score +7 points")
    print("The game ends after 7 possessions you had.")
    print("The team with more points wins the Super Bowl!")
    print("If the game's tied after 7 possessions it will go into overtime!")
    print("Whoever scores first in overtime wins it all!\n")
    print("Explanation of abbreviations:")
    print("TD: Touchdown")
    print("Positions: QB (Quarterback), TE (Tight End), WR (Wide Receiver)\n")
    game_rules_navigation()


def game_rules_navigation():
    """
    Function to let user navigate back to the main menu or
    start the game while in the rules.
    """
    while True:
        print("Do you want to start the game now")
        print("or go back to the welcome menu?")
        print(f"{Fore.YELLOW}1. {Fore.WHITE}Start the game")
        print(f"{Fore.YELLOW}2. {Fore.WHITE}Welcome menu\n")
        user_choice_rules = input(f"{Fore.YELLOW}Your choice (1/2):\n")
        clear()

        if user_choice_rules == "1":
            print(f"{Fore.WHITE}Let the games begin...")
            time.sleep(2)
            start_game()
            break
        elif user_choice_rules == "2":
            welcome()
            break
        else:
            print(
                f"{Fore.RED}{user_choice_rules} is an invalid input. "
                "Please choose again."
            )


def start_game():
    """
    Function to start the game.
    The game starts with the first decission: the cointoss!
    """
    print("Welcome to the Super Bowl, ")
    print("the most prestigious sporting event of the year!")
    print(
        f"--- {Fore.BLUE}New York Giants {Fore.WHITE}: "
        f"{Fore.RED}Kansas City Chiefs {Fore.WHITE}---"
    )
    print("It's time for the game to begin, but who will get the ball first ")
    print("and the chance to score the first points?")
    print("It's your turn!\n")
    cointoss_start_game()


def cointoss_start_game():
    """
    Function to start the game with the first decission: the cointoss!
    """
    while True:
        print("\nDo you want to choose Heads or Tails?")
        print(f"{Fore.YELLOW}1. {Fore.WHITE}Heads")
        print(f"{Fore.YELLOW}2. {Fore.WHITE}Tails")

        user_choice_cointoss = input(f"{Fore.YELLOW}Your choice (1/2):\n")
        clear()

        if user_choice_cointoss in ("1", "2"):
            break
        else:
            print(
                f"{Fore.RED}{user_choice_cointoss} is an invalid input. "
                "Please choose again."
            )

    num = random.randint(1, 2)
    result = str(num)

    if user_choice_cointoss == result:
        print(
            f"{Fore.WHITE}Congrats! "
            "Your first win, now let's get started..."
        )
        time.sleep(2)
        giants_possession()
    else:
        print(
            f"{Fore.WHITE}Aw...You've lost the cointoss, "
            "but that means nothing!\n"
        )
        time.sleep(2)
        chiefs_posession()


# Variables as Data for scoreboard
chiefs_scored_points = 0
giants_scored_point = 0


def chiefs_posession():
    """
    Function when chiefs are in posession. USER HAS NO CONTROL!
    """
    # Zugriff auf die globale Variable
    global chiefs_scored_points
    global giants_scored_point

    print("Current Score:")
    print(
        f"--- {Fore.BLUE}New York Giants {Fore.WHITE}{giants_scored_point} : "
        f"{chiefs_scored_points} {Fore.RED}Kansas City Chiefs {Fore.WHITE}---"
    )
    print("The Chiefs are in posession...\n")
    time.sleep(2)
    if random.random() < 0.5:
        print("The Chiefs score a TD!")
        print("Now it's your turn! Go get some points...\n")
        chiefs_scored_points += 7
        time.sleep(2)
        giants_possession()
    elif random.random() < 0.5:
        print("Your defense held and forced a turnover on downs!")
        print("Now it's your turn! Go get some points...\n")
        time.sleep(2)
        giants_possession()
    else:
        print("Your defense has achieved a turnover!")
        print("Now it's your turn! Go get some points...\n")
        time.sleep(2)
        giants_possession()


user_possession_counter = 0


def giants_possession():
    """
    Function when the Giants (The User) is in possession of the ball
    with random starting position and yard line.
    """

    global user_possession_counter

    user_possession_counter += 1

    print("Current Score:")
    print(
        f"--- {Fore.BLUE}New York Giants {Fore.WHITE}{giants_scored_point} : "
        f"{chiefs_scored_points} {Fore.RED}Kansas City Chiefs {Fore.WHITE}---"
    )
    time.sleep(2)

    if user_possession_counter == 7:
        print("\nThis is your last possession - Make it count!")
    else:
        print(f"Possession: {user_possession_counter} / 7")

    yard_line = random.randint(15, 50)
    starting_position = random.choice(["own", "opponents"])

    print(f"You start at your {starting_position} {yard_line} Yard line!")
    giants_posession_choose_play()


# variable to stop possession if 4 incompletions in a row accure
consecutive_incomplete_pass = 0


def giants_posession_choose_play():
    """
    Function for user to decide what play to be played.
    """
    # Zugriff auf die globale Variable
    global chiefs_scored_points
    global giants_scored_point
    global user_possession_counter
    global consecutive_incomplete_pass

    while True:
        print("\nWhich play do you choose?")
        print(f"{Fore.YELLOW}1. {Fore.WHITE}Long Pass to WR")
        print(f"{Fore.YELLOW}2. {Fore.WHITE}Short Pass to WR")
        print(f"{Fore.YELLOW}3. {Fore.WHITE}Short Pass to TE")

        qb_choice = input(f"{Fore.YELLOW}Your choice (1/2/3):\n")
        clear()
        if qb_choice in ["1", "2", "3"]:
            break
        else:
            print(f"{Fore.RED}{qb_choice} isn't valid. Please try again!")

    if qb_choice == "1":
        if random.random() <= 0.2:
            if user_possession_counter == 7:
                print("OH NOOOO! You're pass has been intercepted! ")
                print("This was your last drive...")
                time.sleep(2)
                end_game()
            else:
                print("OH NOOOO! You're pass has been intercepted! ")
                print("Now the Chiefs have the ball!")
                print("Keep ypur head up! Take a breather ")
                print("and come back stronger after their posession!\n")
                time.sleep(2)
                chiefs_posession()
        elif random.random() <= 0.4:
            print("Congrats! You've scored a TOUCHDOWN!")
            if user_possession_counter == 7:
                print("This was your last drive...")
                giants_scored_point += 7
                time.sleep(2)
                end_game()
            else:
                print("Take a breather while the Chiefs are on offense...\n")
                giants_scored_point += 7
                time.sleep(2)
                chiefs_posession()
        elif random.random() <= 0.6:
            print("Incomplete pass! The Chiefs defense has blocked your pass!")
            consecutive_incomplete_pass += 1
            if consecutive_incomplete_pass == 4:
                if user_possession_counter == 7:
                    print("Four consecutive incomplete passes! ")
                    print("This was your last drive...")
                    time.sleep(2)
                    end_game()
                else:
                    print("Four consecutive incomplete passes! ")
                    print("Chiefs take possession.")
                    time.sleep(2)
                    chiefs_posession()
            else:
                giants_posession_choose_play()
        else:
            print("Completion! You achieved a new first down ")
            print(f"{Fore.YELLOW}and move further down the field!")
            # reset to zero with new first down
            consecutive_incomplete_pass = 0
            giants_posession_choose_play()
    elif qb_choice == "2":
        if random.random() <= 0.2:
            if user_possession_counter == 7:
                print("OH NOOOO! You're pass has been intercepted! ")
                print("This was your last drive...")
                time.sleep(2)
                end_game()
            else:
                print("OH NOOOO! You're pass has been intercepted! ")
                print("Now the Chiefs have the ball!")
                print("Keep ypur head up! Take a breather ")
                print("and come back stronger after their posession!\n")
                time.sleep(2)
                chiefs_posession()
        elif random.random() <= 0.4:
            print("Congrats! You've scored a TOUCHDOWN!")
            if user_possession_counter == 7:
                print("This was your last drive...")
                giants_scored_point += 7
                time.sleep(2)
                end_game()
            else:
                print("Take a breather while the Chiefs are on offense...\n")
                giants_scored_point += 7
                time.sleep(2)
                chiefs_posession()
        elif random.random() <= 0.5:
            print("Incomplete pass! The Chiefs defense has blocked your pass!")
            consecutive_incomplete_pass += 1
            if consecutive_incomplete_pass == 4:
                if user_possession_counter == 7:
                    print("Four consecutive incomplete passes! ")
                    print("This was your last drive...")
                    time.sleep(2)
                    end_game()
                else:
                    print("Four consecutive incomplete passes! ")
                    print("Chiefs take possession.")
                    time.sleep(2)
                    chiefs_posession()
            else:
                giants_posession_choose_play()
        else:
            print("Completion! You achieved a new first down ")
            print(f"{Fore.YELLOW}and move further down the field!")
            # reset to zero with new first down
            consecutive_incomplete_pass = 0
            giants_posession_choose_play()
    else:
        if random.random() <= 0.2:
            if user_possession_counter == 7:
                print("OH NOOOO! You're pass has been intercepted! ")
                print("This was your last drive...")
                time.sleep(2)
                end_game()
            else:
                print("OH NOOOO! You're pass has been intercepted! ")
                print("Now the Chiefs have the ball!")
                print("Keep ypur head up! Take a breather ")
                print("and come back stronger after their posession!\n")
                time.sleep(2)
                chiefs_posession()
        elif random.random() <= 0.4:
            print("Congrats! You've scored a TOUCHDOWN!")
            if user_possession_counter == 7:
                print("This was your last drive...")
                giants_scored_point += 7
                time.sleep(2)
                end_game()
            else:
                print("Take a breather while the Chiefs are on offense...\n")
                giants_scored_point += 7
                time.sleep(2)
                chiefs_posession()
        elif random.random() <= 0.5:
            print("Incomplete pass! The Chiefs defense has blocked your pass!")
            consecutive_incomplete_pass += 1
            if consecutive_incomplete_pass == 4:
                if user_possession_counter == 7:
                    print("Four consecutive incomplete passes! ")
                    print("This was your last drive...")
                    time.sleep(2)
                    end_game()
                else:
                    print("Four consecutive incomplete passes! ")
                    print("Chiefs take possession.")
                    time.sleep(2)
                    chiefs_posession()
            else:
                giants_posession_choose_play()
        else:
            print("Completion! You achieved a new first down ")
            print(f"{Fore.YELLOW}and move further down the field!")
            # reset to zero with new first down
            consecutive_incomplete_pass = 0
            giants_posession_choose_play()


def end_game():
    """
    Function for the end of the game.
    """
    print("\nTHIS IS THE END!")
    print(
        f"--- {Fore.BLUE}New York Giants {Fore.WHITE}{giants_scored_point} : "
        f"{chiefs_scored_points} {Fore.RED}Kansas City Chiefs {Fore.WHITE}---"
    )
    if giants_scored_point > chiefs_scored_points:
        print("Congratulations! You win the Super Bowl! ")
        print("You are a world champion!\n")
        time.sleep(2)
        print("This is the end of the game...")
        print("I hope you had as much fun playing it as i had programming it!")
        end_game_navigation()
    elif giants_scored_point < chiefs_scored_points:
        print("Unfortunately, you lose the Super Bowl. ")
        print("Better luck next time!\n")
        time.sleep(2)
        print("This is the end of the game...")
        print("I hope you had as much fun playing it as i had programming it!")
        end_game_navigation()
    else:
        print("No winner after regulation!")
        start_overtime()


def start_overtime():
    """
    Function for overtime to start, when game ended in a draw
    """
    print("It's overtime! The first team to score wins. ")
    print("Let's start with a coin toss.")
    coin_toss_overtime()


def chiefs_posession_overtime():
    """
    Function for chiefs possession in overtime.
    """
    # Zugriff auf die globale Variable
    global chiefs_scored_points
    global giants_scored_point

    if random.random() < 0.5:
        print("The Chiefs scored a TOUCHDOWN...")
        print("Unfortunately that means that you have lost...")
        chiefs_scored_points += 7
        time.sleep(2)
        end_game_after_overtime()
    else:
        print("The Chiefs did not score. ")
        print("Now it's your chance to win it all!\n")
        time.sleep(2)
        giants_possession_overtime()


def giants_possession_overtime():
    """
    Function for the user possession to start.
    """
    yard_line = random.randint(15, 50)
    starting_position = random.choice(["own", "opponents"])

    print(f"You start at your {starting_position} {yard_line} Yard line!")
    giants_posession_choose_play_overtime()


# variable to stop possession if 4 incompletions in a row accure
consecutive_incomplete_pass_overtime = 0


def giants_posession_choose_play_overtime():
    """
    Function for the user qb choices in overtime.
    """
    # Zugriff auf die globale Variable
    global chiefs_scored_points
    global giants_scored_point
    global consecutive_incomplete_pass_overtime

    while True:
        print("\nWhich play do you choose?")
        print(f"{Fore.YELLOW}1. {Fore.WHITE}Long Pass to WR")
        print(f"{Fore.YELLOW}2. {Fore.WHITE}Short Pass to WR")
        print(f"{Fore.YELLOW}3. {Fore.WHITE}Short Pass to TE")

        qb_choice = input(f"{Fore.YELLOW}Your choice (1/2/3):\n")
        clear()
        if qb_choice in ["1", "2", "3"]:
            break
        else:
            print(f"{Fore.RED}{qb_choice} isn't valid. Please try again!")

    if qb_choice == "1":
        if random.random() <= 0.2:
            print("OH NOOOO! You're pass has been intercepted! ")
            print("Now the Chiefs have the ball!")
            print("Keep ypur head up! Take a breather ")
            print("and come back stronger after their posession!\n")
            time.sleep(2)
            chiefs_posession_overtime()
        elif random.random() <= 0.4:
            print("Congrats! You've scored a TOUCHDOWN!")
            print("\nThis is it! You've won the Super Bowl!")
            giants_scored_point += 7
            end_game_after_overtime()
        elif random.random() <= 0.6:
            print("Incomplete pass! The Chiefs defense has blocked your pass!")
            consecutive_incomplete_pass_overtime += 1
            if consecutive_incomplete_pass_overtime == 4:
                print("Four consecutive incomplete passes! ")
                print("Chiefs take possession.")
                time.sleep(2)
                chiefs_posession_overtime()
            else:
                giants_posession_choose_play_overtime()
        else:
            print("Completion! You achieved a new first down ")
            print(f"{Fore.YELLOW}and move further down the field!")
            # reset to zero with new first down
            consecutive_incomplete_pass_overtime = 0
            giants_posession_choose_play_overtime()
    elif qb_choice == "2":
        if random.random() < 0.2:
            print("OH NOOOO! You're pass has been intercepted! ")
            print("Now the Chiefs have the ball!")
            print("Keep ypur head up! Take a breather ")
            print("and come back stronger after their posession!\n")
            time.sleep(2)
            chiefs_posession_overtime()
        elif random.random() < 0.4:
            print("Congrats! You've scored a TOUCHDOWN!")
            print("\nThis is it! You've won the Super Bowl!")
            giants_scored_point += 7
            end_game_after_overtime()
        elif random.random() < 0.5:
            print("Incomplete pass! The Chiefs defense has blocked your pass!")
            consecutive_incomplete_pass_overtime += 1
            if consecutive_incomplete_pass_overtime == 4:
                print("Four consecutive incomplete passes! ")
                print("Chiefs take possession.")
                time.sleep(2)
                chiefs_posession_overtime()
            else:
                giants_posession_choose_play_overtime()
        else:
            print("Completion! You achieved a new first down ")
            print(f"{Fore.YELLOW}and move further down the field!")
            # reset to zero with new first down
            consecutive_incomplete_pass_overtime = 0
            giants_posession_choose_play_overtime()
    else:
        if random.random() < 0.2:
            print("OH NOOOO! You're pass has been intercepted! ")
            print("Now the Chiefs have the ball!")
            print("Keep ypur head up! Take a breather ")
            print("and come back stronger after their posession!\n")
            time.sleep(2)
            chiefs_posession_overtime()
        elif random.random() < 0.4:
            print("Congrats! You've scored a TOUCHDOWN!")
            print("\nThis is it! You've won the Super Bowl!")
            giants_scored_point += 7
            end_game_after_overtime()
        elif random.random() < 0.5:
            print("Incomplete pass! The Chiefs defense has blocked your pass!")
            consecutive_incomplete_pass_overtime += 1
            if consecutive_incomplete_pass_overtime == 4:
                print("Four consecutive incomplete passes! ")
                print("Chiefs take possession.")
                time.sleep(2)
                chiefs_posession_overtime()
            else:
                giants_posession_choose_play_overtime()
        else:
            print("Completion! You achieved a new first down ")
            print(f"{Fore.YELLOW}and move further down the field!")
            # reset to zero with new first down
            consecutive_incomplete_pass_overtime = 0
            giants_posession_choose_play_overtime()


def coin_toss_overtime():
    """
    Function for the cointoss in overtime.
    """
    while True:
        print("\nDo you want to choose Heads or Tails?")
        print(f"{Fore.YELLOW}1. {Fore.WHITE}Heads")
        print(f"{Fore.YELLOW}2. {Fore.WHITE}Tails")

        user_choice_cointoss_overtime = input(
            f"{Fore.YELLOW}Your choice (1/2):\n"
        )
        clear()

        if user_choice_cointoss_overtime in ("1", "2"):
            break
        else:
            print(
                f"{Fore.RED}{user_choice_cointoss_overtime} "
                "is an invalid input. Please choose again."
            )

    num_overtime = random.randint(1, 2)
    result = str(num_overtime)

    if user_choice_cointoss_overtime == result:
        print(
            f"{Fore.WHITE}Congrats! "
            "You win, you get the ball to start the overtime!\n")
        giants_possession_overtime()
        time.sleep(2)
    else:
        print(f"{Fore.WHITE}Aw...You've lost the cointoss!\n")
        print("The Chiefs are taking over to start the overtime...\n")
        time.sleep(2)
        chiefs_posession_overtime()


def end_game_after_overtime():
    """
    Function to end the game after overtime.
    """
    print("\nTHIS IS THE END!")
    print(
        f"--- {Fore.BLUE}New York Giants {Fore.WHITE}{giants_scored_point} : "
        f"{chiefs_scored_points} {Fore.RED}Kansas City Chiefs {Fore.WHITE}---"
    )
    if giants_scored_point > chiefs_scored_points:
        print("Congratulations! You win the Super Bowl! ")
        print("You are a world champion!\n")
        time.sleep(2)
        print("This is the end of the game...")
        print("I hope you had as much fun playing it as i had programming it!")
    else:
        print("Unfortunately, you lose the Super Bowl. ")
        print("Better luck next time!\n")
        time.sleep(2)
        print("This is the end of the game...")
        print("I hope you had as much fun playing it as I had programming it!")

    end_game_navigation()


def end_game_navigation():
    """
    Function to let user navigate back to the main menu.
    """
    global giants_scored_point
    global chiefs_scored_points
    global user_possession_counter
    global consecutive_incomplete_pass
    global consecutive_incomplete_pass_overtime

    print("Head back to the main menu and end this game!")
    input_end_game_navigation = input(
        f"Hit {Fore.YELLOW}ENTER {Fore.WHITE}to end game"
    )
    clear()

    print("See you next time!\n")
    time.sleep(2)

    # reset everything to 0 in case the user plays again!
    giants_scored_point = 0
    chiefs_scored_points = 0
    user_possession_counter = 0
    consecutive_incomplete_pass = 0
    consecutive_incomplete_pass_overtime = 0
    welcome()


if __name__ == "__main__":
    """
    Initialise the app.
    """
    clear()
    welcome()
