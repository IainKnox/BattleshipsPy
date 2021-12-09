"""
Battleships Game

When running the terminal, players are welcomed to the game,
given the option to review the offical rules on how to play the game
or enter their name and proceed to start.
"""

print("\033[0;37;40m Welcome to \033[1;34;40m BattleshipsPY \033[0;37;40m \n")
print("Would you like to review the game instructions? Press Y or N\n")
instructions = input().lower()

game_rules = """
    1) Be the first to sink all 5 of your opponents ships.
    2) Place a fleet of 5 ships across the ocean grid.
        Rules for placing ships:
        2.1) Place each ship in any horizontal or vertical line,
             but not diagonally.
        2.2) Do not place a ship so that it overlaps another ship,
             or the edge of the grid.
        2.3) Do not change the position of ship once the 
             game has begun.
    3) You and your opponent will alternate turns, calling out
        one shot per turn to try and Hit each others ships.
    4) On your turn, designate a co-ordinate to fire upon.
        For example D-5. Your opponent will confirm whether 
        the shot is a Hit or Miss.
    5) If you call a shot occupied by your opponents ocean grid,
        it is considered a Hit. You opponent will confirm which vessel
        is hit and mark with a red 'H'
    6) If you call a shot not occupied by your opponent ocean grid,
        it is considered a Miss. This is marked with a blue 'M'
    7) Once all the co-ordinates of any one ship have been Hit, it is 
        considered as Sunk and all 'H' markers are changed to 'S'.
    8) If you are the first player to sink your oppoents entire fleet,
        you win the game!
"""


while instructions != "y" and instructions != "n":
    # test to see whether the user has pressed Y or N
    # and convert to lowercase. If incorrect value is
    # chosen, the throw error and repeat till valid
    # answer is given.
    print("Your seleciton is invalid, Please enter Y for 'Yes' and N for 'No'\n")
    instructions = input().lower()
else:
    if instructions == "n":
        print("Let's set up the game board\n")
    else:
        print(game_rules)

# game_board = [["¦  ¦"for x in range(8)] for y in range(8)]
# for i in game_board:
#     print("\033[1;32;40m --   --   --   --   --   --   --   --")
#     print(" ".join(i))
#     print(" --   --   --   --   --   --   --   --\033[0;37;40m")

from string import ascii_uppercase as letters
letter = list(letters[:10])
num = iter(range(0,9))

game_board = [["0" for x in range(10)] for y in range(10)]
print("   " + " ".join(letter))
for row in game_board:
    print(next(num), end="¦ ")
    print(" ".join(row))





# game_board = []
# def print_board(game_board):
#     print("  0, 1, 2, 3, 4, 5, 6, 7, 8, 9")
#     print(" -- " * 10)
#     for row in range(10):
#         game_board.append(" [] "* 10)
#     letter = 0
#     for letter in range(10):
#         print(chr(letter + 65), end=" ¦")
#         for column in range(len(game_board[letter])):
#             print(game_board[letter][column], end="")
#         print("¦ ")
#         letter += 1
#     print("--   " * 10)

# print_board(game_board)
        