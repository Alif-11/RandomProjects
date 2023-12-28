# Handles taking user inputs
# and acts as a driver file for the other scripts files.

import display


def game_text():
    # Tested
    user_input = input(
        "Enter 1 to play the game.\nEnter 2 to see your personal leaderboard.\n")
    try:
        num = int(user_input)
    except:
        print("You did not input a number. Please try again.")
        game_text()
    else:
        match num:
            case 1:
                print("Game Start!")
                display.print_topline()
            case 2:
                print("Displaying Leaderboard!")
            case _:
                print(
                    "A number was chosen that was not on the item list. Please try again.")
                game_text()


def play_game():
    # Tested
    print("Welcome to Big-Tac-Toe!\nWhat would you like to do?")
    game_text()


# Self - Note: If we are running this file.
if __name__ == "__main__":
    # Tested
    play_game()
