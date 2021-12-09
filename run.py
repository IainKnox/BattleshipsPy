"""
Battleships Game

When running the terminal, players are welcomed to the game,
given the option to review the offical rules on how to play the game
or enter their name and proceed to start.
"""

print("Welcome to BattleshipsPY\n")
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
    """
    test to see whether the user has pressed Y or N
    and convert to lowercase. If incorrect value is
    chosen, the throw error and repeat till valid
    answer is given.
    """
    print("Your seleciton is invalid, Please enter Y for 'Yes' and N for 'No'\n")
    instructions = input().lower()
else:
    if instructions == "n":
        print("Let's set up the game board\n")
        break
    else:
        print(game_rules)
