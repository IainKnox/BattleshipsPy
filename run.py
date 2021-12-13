"""
Battleships Game

When running the terminal, players are welcomed to the game,
given the option to review the offical rules on how to play the game
or enter their name and proceed to start.

Game structure:

* player vs computer game, where player can place 5 ships on a 10x10grid.
* computer places ships using random.
* 2 phases for the game, 1)Setup grid and 2)Missle firing.
* in the Setup phase, check for legal vs illegal moves.
* legal move would be (x,y) axis either vertically or horizontally.
* illegal move would be the intersection of ships, or going off grid.
* the Missle firing phase would be checking miss vs hits and sink.
* player starts with a set amount of missles to add a layer of difficulty
* which are decremented irrespective of hit or miss.

Legend:

"B" - represents a section of the Battleship
"H" - represents a hit
"S" - represents sunk
"M" - represents a miss
"." - represents an water or a empty part of the ocean grid
"""

from string import ascii_uppercase as letters
letter = list(letters[:10])  # create a list of letters to use on the ocean grid.
# look at possibility of user defining a board size to a max. of 26 letters
missle = 10  # number of missles set when game is initialized, set to 10 for testing purposes
import time
import os
import random


#  TODO [ ] define the 2 game phases. setup phase and missle firing phase
#  TODO [x] define what a Battleship is. what's its name, how long is it?
#  TODO [x] create an array to hold the Battleships
#  TODO [ ] allow the player to place the ships on the grid.
#  TODO [ ] define ship placement. starting position, grid boundries, illegal moves
#  TODO [ ] define hit, miss and sunk
#  TODO [ ] define scoring, and a win or lose condition resulting in endgame.
#  TODO [ ] add some ASCII artwork to fancy it up


def valid_name(player):
    """
    create a function to validate the player's chosen name, ensuring
    they have entered one and that it's not over 10 characters long.
    """
    if len(player) > 10:
        print("Asked you not to go over 10 Characters!")
        return False
    elif len(name) == 0:
        print("You'll need to speak up, didn't quite get that.")
    else:
        return True


def player():
    """
    create a player class that asks for a name, stored in a variable
    that is used to tell who's board is in play.
    """
    print("Welcome to BattleshipPY\n")
    print("Enter the name of your Fleet: \n ")
    while True:
        player_name = input("Nothing too fancy mind, Maximum of 10 characters please.\n").upper()
        if valid_name(player_name):
            break
    print(f"You shall be known as: {player_name}\n")
    time.sleep(1)
    print(f"Alright {player_name}, let's prepare for War!")
    return player_name


# Rules taken from official Battleships documentation
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


instructions = input("Would you like to review the game rules? Y or N\n").lower()
while instructions != "y" and instructions != "n":
    instructions = input("\nCome again? Please enter y for yes or n for no.\n> ").lower()
else:
    if instructions == "n":
        print("\nLooks like we are good to go.\n")
    else:
        print(game_rules)
        time.sleep(2)
        input("press ENTER to continue\n")  # give the user time to read over the rules


class gameboard():
    """
    create a gameboard class used to initialize a fully operational
    gameboard that has width, height and ships.
    """

    def __init__(self, width, height, ships):
        """
        define what makes a game board and create
        an array to store all the missle co ordinates fired
        in the shots array.
        """
        self.width = width
        self.height = height
        self.ships = ships
        self.shots = []

    def take_shots(self, shot_location):
        """
        update the various ships with hits and
        save the fact that a shot was either a Hit or Miss
        """
        pass

    def is_game_over(self):
        """
        define what constitutes the game over conditions.
        iterate through the ships and check if they have been
        destroyed.
        """
        pass


class ships(object): 
    """
    create a ship class used to build all ships from
    a ship is constructed of a name/type, lenght, status(hit/destroyed)
    """
    @staticmethod  # create the build method on the class and not the instance
    def build(start, length, direction):
        """
        each instance of the all_ship class has a starting point,
        a lenght and a direction
        """
        body = []
        for i in range(length):
            if direction == "U":  #up
                part = (start[0], start[1] -i)  #minus 1 from y co-ord
            elif direction == "D":  #down
                part = (start[0], start[1] +i)  #add 1 to y co-ord
            elif direction == "L":  #left
                part = (start[0] -i, start[1])  #minus 1 from x co-ord
            elif direction == "R":  #right
                part = (start[0] +i, start[1])  #add 1 to x co-ord

            body.append(part)
        return ships(body, direction)
        # syntax for constucting a battleship --> b.ships.build((1,2), 2, "U")

    def __init__(self, body, direction):  #co-ords are the location of the ship object
        self.body = body
        self.direction = direction
        self.hits = [False] * len(body)

    def body_index(self, location):
        try:
            return self.body.index(location)
        except ValueError:
            return None

    def is_sunk(self):
        """
        test the ship to see if all co-ords in the array have been hit
        resulting in a sunk ship.
        """
        return all(self.hits)


def game_board(width, height):

    print("+ " + "  ".join(letter) + " +")
    header = ("+" + "---" * width + "+")
    print(header)
    game_board = []

    for i in range(height):
        print("¦" + "   " * width + "¦")
    print(header)
# game_board = [["0" for x in range(10)] for y in range(10)]

# def main():
#     game_board(10, 10)
#     battleship = [
#         ships.build((1,2), 2, "U"),
#         ships.build((5,8), 5, "U"),
#         ships.build((2,3), 3, "E"),
#     ]

#     for b in battleship:
#         print(b.body)

# main()
# #game loop

# play = True
# while play and missle > 0:
#     game_board(10,10)

#create an input for user to enter co-ordinates to fire missle at
# based on difficulty, the player will have a set number of shots eg. 75/50/25
# built functionality around whether missles hit, miss or sink opponents ships
#     if missle > 0:
#         fire_missle = input(" Enter launch co-ordinate (eg.A4): \n")
#         x, y = fire_missle.split(",")
#         #firing sequence letter then number (A,4)
#         game_board[int(fire_missle[1])-1][letter.index(fire_missle[0])] = "x"
#         missle =-1
#         print(f"you have {missle} missles left.\n")
#     else:
#         print("You are out of missles.\n")
def draw_ships(width, height, ships):
    header = ("+" + "---" * width + "+")
    print(header)

    #empty game_board
    game_board = []
    for x in range(width):
        row = []
        for y in range(height):
            row.append(None)
        game_board.append(row)
    
    # add ships to board
    for b in ships:
        for x, y in b.body:
            game_board[x][y] = "B"
    
    for y in range(height):
        row = []
        for x in range(width):
            row.append(game_board[x][y]) or " "
        print(" ".join(row))

    print(header)



if __name__ == "__main__":

    battleship = [
         ships.build((1,2), 2, "U"),
         ships.build((5,8), 5, "U"),
         ships.build((2,3), 3, "R"),
     ]

    for b in battleship:
        print(b.body)
    draw_ships(10, 10, ships)
