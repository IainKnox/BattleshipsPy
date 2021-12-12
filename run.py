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
"""


import time
import os
import random


#TODO [ ] define the 2 game phases. setup phase and missle firing phase
#TODO [x] define what a Battleship is. what's its name, how long is it?
#TODO [x] create an array to hold the Battleships
#TODO [ ] allow the player to place the ships on the grid.
#TODO [ ] define ship placement. starting position, grid boundries, illegal moves
#TODO [ ] define hit, miss and sunk
#TODO [ ] define scoring, and a win or lose condition resulting in endgame.
#TODO [ ] add some ASCII artwork to fancy it up


print("Welcome to BattleshipsPY\n")
name = input("Please enter you name Captain: \n")

while name == "":
    print("You'll need to speak up, didn't quite get that.")
    name = input("Please enter your name Captain: \n")
else:
    print(f"alright {name}, let's prepare for war\n")


#instructions = input("Would you like to review the game instructions? Press Y or N\n").lower()
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


class all_ships:
    """
    create a ship class used to build all ships from
    a ship is constructed of a name/type, lenght, status(hit/destroyed)
    """
    @staticmethod #create the build method on the class and not the instance
    def build(start, lenght, direction):
        """
        each instance of the all_ship class has a starting point,
        a lenght and a direction
        """
        co_ords = []
        for i in range(length):
            if direction == "U": #up
                body = (start[0], start[1] -1) #minus 1 from y co-ord
            elif direction == "D": #down
                body = (start[0], start[1] +1) #add 1 to y co-ord
            elif direction == "L": #left
                body = (start[0] -1, start[1]) #minus 1 from x co-ord
            elif direction == "R": #right
                body = (start[0] +1, start[1]) #add 1 to x co-ord
            co_ords.append(body)
        return all_ships(co_ords, direction)

    def __init__(self, co_ords, direction): #co-ords are the location of the ship object
        self.co_ords = co_ords
        self.direction = direction
        self.hits = [False] * len(co_ords)

    def co_ords_index(self, location):
        try:
            return self.co_ords.index(location)
        except ValueError:
            return None
    def is_sunk(self):
        return all(self.hits)




# game_board = [["¦  ¦"for x in range(8)] for y in range(8)]
# for i in game_board:
#     print("\033[1;32;40m --   --   --   --   --   --   --   --")
#     print(" ".join(i))
#     print(" --   --   --   --   --   --   --   --\033[0;37;40m")


from string import ascii_uppercase as letters
letter = list(letters[:10]) #create a list of letters to use on the ocean grid.
# look at possibility of user defining a board size to a max. of 26 letters


missle = 10 # number of missles set when game is initialized, set to 10 for testing purposes

def game_board(width, height):

    print("+ " + "  ".join(letter) + " +")
    header = ("+" + "---" * width + "+")
    print(header)
    game_board = []

    for i in range(height):
        print("¦" + "   " * width + "¦")
    print(header)

# game_board = [["0" for x in range(10)] for y in range(10)]

game_board(10, 10)










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
