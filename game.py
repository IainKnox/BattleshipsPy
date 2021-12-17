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
"~" - represents a miss
"~" - represents an water or a empty part of the ocean grid
"""

from string import ascii_uppercase as letters
letter = list(letters[:10])  # create a list of letters to use on the ocean grid.
# look at possibility of user defining a board size to a max. of 26 letters
missle = 10  # number of missles set when game is initialized, set to 10 for testing purposes
import time
import os
import random

class Oceangrid:
    """
    create a ocean grid/game board class used to initialize a fully operational
    board that has width, height and ships.
    """

    def __init__(self, width, height, battleships):
        """
        define what makes a game board and create
        an array to store all the missle co ordinates fired
        in the shots array.
        """
        self.width = width
        self.height = height
        self.battleships = battleships 
        self.missles = []

    def shoot(self, missle_location): #take shots
        """
        update the various ships with hits taken and
        save the fact that a shot was either a Hit or Miss
        """
        is_hit = False
        for b in self.battleships:
            index = b.body_index(missle_location)  # return the index of the shot location
            if index is not None:
                is_hit = True
                b.hits[index] = True
                break

        self.missles.append(Hits(missle_location, is_hit))


    def is_game_over(self):
        """
        define what constitutes the game over conditions.
        iterate through the ships and check if they have been
        destroyed.
        """
        pass


class Hits:  #shots
    """
    create a simple class to store information regarding whether
    a missle location was a hit or not.
    """
    def __init__(self,location, is_hit):
        self.location = location
        self.is_hit = is_hit


class Battleship:
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
        return Battleship(body, direction)
        # syntax for constucting a battleship --> b.ships.build((1,2), 2, "U")

    def __init__(self, body, direction):  #co-ords are the location of the ship object
        """
        create a function that stores information regarding hits taken
        in terms of the length of the ship. With hits being changed
        to True when a hit is registered. 
        """ 
        self.body = body
        self.direction = direction
        self.hits = [False] * len(body)  
        # eg[False][False][True] <-- represents 1 hit on a 3 block ship

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


def draw_board(game_board, debug_mode = False):
    header = ("+" + "-" * game_board.width + "+")
    print(header)

    # empty game_board
    board = []
    for x in range(game_board.width):
        board.append([None for y in range(game_board.height)])

    # add ships to board
    if debug_mode:
        for b in game_board.battleships:
            for x, y in b.body:
                board[x][y] = "B"

    # add missles to the board
    for sh in game_board.missles:
        x, y = sh.location
        if sh.is_hit:
            m = "X"
        else:
            m = "."
        board[x][y] = m

    for y in range(game_board.height):
        row = []
        for x in range(game_board.width):
            row.append(board[x][y] or " ")
        print("¦" + "".join(row)+ "¦")
    print(header) 


if __name__ == "__main__":
    battleships = [
         Battleship.build((1,1), 2, "U"),
         Battleship.build((5,8), 5, "U"),
         Battleship.build((2,3), 3, "R"),
    ]  # hardcoded for debugging

    for b in battleships:
        print(b.body)

    game_board = Oceangrid(10, 10, battleships)


    while True:
        fire_missle = input("Enter your launch co-ordinates: (eg. 1,1)\n")
        xstr, ystr = fire_missle.split(",")
        x = int(xstr)
        y = int(ystr)
        print(fire_missle)

        game_board.shoot((x,y))
        draw_board(game_board)
