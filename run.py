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
import time
import os
import random
import copy
from string import ascii_uppercase as letters
letter = list(letters[:10])
# create a list of letters for ocean grid.
# look at possibility of user defining a board size to a max. of 26 letters
shot_count = 10  # no of missles when game starts, 10 for testing purposes
ship_sunk = 0


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
        is hit and mark with a 'H'
    6) If you call a shot not occupied by your opponent ocean grid,
        it is considered a Miss. This is marked with a '~'
    7) Once all the co-ordinates of any one ship have been Hit, it is
        considered as Sunk.
    8) If you are the first player to sink your opponents entire fleet,
        you win the game!
"""


class Oceangrid:
    """
    create a ocean grid/game board class used to initialize a fully operational
    board that has width, height and ships.
    """

    def __init__(self, battleships, width, height):
        """
        define what makes a game board and create
        an array to store all the missle co ordinates fired
        in the shots array.
        """
        self.battleships = battleships
        self.missles = []
        self.width = width
        self.height = height

    def shoot(self, missle_location):
        # take shots
        """
        update the various ships with hits taken and
        save the fact that a shot was either a Hit or Miss
        """
        hit_battleship = None
        is_hit = False
        for b in self.battleships:
            index = b.body_index(missle_location)  # index of the shot location
            if index is not None:
                is_hit = True
                b.hits[index] = True
                hit_battleship = b
                break

        self.missles.append(Hits(missle_location, is_hit))
        return hit_battleship

    def is_game_over(self):
        """
        define what constitutes the game over conditions.
        iterate through the ships and check if they have been
        destroyed.
        """
        for b in self.battleships:
            if not b.is_sunk():
                return False
            return True


class Hits:
    # shots
    """
    create a simple class to store information regarding whether
    a missle location was a hit or not.
    """
    def __init__(self, location, is_hit):
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
            # up minus 1 from y co-ord
            if direction == "U":
                part = (start[0], start[1] - i)
            # down add 1 to y co-ord
            elif direction == "D":
                part = (start[0], start[1] + i)
            # left  minus 1 from x co-ord
            elif direction == "L":
                part = (start[0] - i, start[1])
            # right add 1 to x co-ord
            elif direction == "R":
                part = (start[0] + i, start[1])

            body.append(part)
        return Battleship(body, direction)
        # syntax for constucting a battleship --> b.ships.build((1,2), 2, "U")

    def __init__(self, body, direction):  # co-ords for location of ship object
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
        ship_sunk = 0
        return all(self.hits)
        ships_sunk += 1


class Player:
    """
    create a player class to define the various players and control
    the flow of moves to progress the game.
    """
    def __init__(self, name, moves):
        self.name = name
        self.moves = moves


def valid_name(player):
    """
    create a function to validate the player's chosen name, ensuring
    they have entered one and that it's not over 10 characters long.
    """
    if len(player) > 10:
        print("Asked you not to go over 10 Characters!")
        return False
    elif len(player) == 0:
        print("You'll need to speak up, didn't quite get that.")
    else:
        return True


def create_player():
    """
    create a player class that asks for a name, stored in a variable
    that is used to tell who's board is in play.
    """
    print("Welcome to BattleshipPY\n")
    print("Please enter your name: \n ")
    while True:
        player_name = input("Nothing too fancy ,Max 10 characters.\n").upper()
        if valid_name(player_name):
            break
    print(f"You shall be known as: {player_name}\n")
    time.sleep(1)
    print(f"Alright {player_name}, let's prepare for War!")
    return player_name


def events(event_type, metadata):
    """
    create a function for handling the various events
    that occur during the gamecfor example game over
    , sinking ships, hits and misses
    """
    if event_type == "game_over":
        print("%s Congratulations, you are Victorious!" % metadata["Player"])
        print(f"You sunk {ship_sunk} ships")
    elif event_type == "player_turn":
        print("%s, it's your turn." % metadata["Player"])
    elif event_type == "ship_sunk":
        print("%s, Destroyed a Ship!!." % metadata["Player"])
    elif event_type == "ship_hit":
        print("%s, you HIT a ship!" % metadata["Player"])
    elif event_type == "miss":
        print("%s, you MISSED." % metadata["Player"])


def computer_move(game_board):
    """
    create a function that defines a very basic version of
    an AI player as the opponent using the random library to move
    """
    x = random.randint(0, game_board.width - 1)
    y = random.randint(0, game_board.height - 1)
    return (x, y)


def player_move(game_board):
    """
    create a function that defines the human moves on the opponent
    board.
    """
    fire_missle = input("Enter your launch co-ordinates: (eg. 1,1)\n")
    xstr, ystr = fire_missle.split(",")
    x = int(xstr)
    y = int(ystr)
    return (x, y)


def draw_board(game_board, debug_mode=True):
    """
    creates a function that calls on the Oceangrid class, defines the
    width and height of the Oceangrid and populates the game board.
    The debug mode feature allows the user to diplay the ships for easy
    debugging by setting the value to True.
    """
    header = ("+" + "-" * game_board.width + "+")

    print(header)

    # empty game_board
    board = []
    for x in range(game_board.width):
        board.append([None for y in range(game_board.height)])

    # add ships to board
    if debug_mode:
        for b in game_board.battleships:
            for d, (x, y) in enumerate(b.body):
                # add a bit of styling to the ships
                # based on the direction their pointing
                if b.direction == "U":
                    parts = ("v", "|", "^")
                elif b.direction == "D":
                    parts = ("^", "|", "v")
                elif b.direction == "L":
                    parts = (">", "=", "<")
                elif b.direction == "R":
                    parts = ("<", "=", ">")
                else:
                    raise "Your compass be broke!"
                if d == 0:
                    part = parts[0]
                elif d == len(b.body) - 1:
                    part = parts[2]
                else:
                    part = parts[1]

                board[x][y] = part

    # add missles to the board
    for sh in game_board.missles:
        x, y = sh.location
        if sh.is_hit:
            m = "H"
        else:
            m = "~"
        board[x][y] = m

    for y in range(game_board.height):
        row = []
        for x in range(game_board.width):
            row.append(board[x][y] or " ")
        print("¦" + "".join(row) + "¦")
    print(header)


if __name__ == "__main__":

    instructions = input("Review the game rules? Yor N\n").lower()
    while instructions != "y" and instructions != "n":
        instructions = input("\nCome again? Enter y or n.\n> ").lower()
    else:
        if instructions == "n":
            print("\nLooks like we are good to go.\n")
        else:
            print(game_rules)
            time.sleep(2)
            # give the user time to read over the rules
            input("press ENTER to continue\n")
            os.system("clear")

    battleships = [
        Battleship.build((1, 1), 2, "L"),
        Battleship.build((5, 8), 5, "U"),
        Battleship.build((4, 0), 3, "R"),
        Battleship.build((7, 6), 3, "D"),
        Battleship.build((2, 9), 4, "R")
    ]  # hardcoded for debugging

    two_player = [      # creates 2 game boards
        Oceangrid(battleships, 10, 10),
        Oceangrid(copy.deepcopy(battleships), 10, 10)  # create copy
    ]

    players = [
        Player(create_player(), player_move),   # human player
        Player("Monty", computer_move)             # computer player
    ]

    attacking_index = 0

    while True:
        defending_index = (attacking_index + 1) % 2
        defending_board = two_player[defending_index]
        attacking_player = players[attacking_index]

        events("player_turn", {"Player": attacking_player.name})
        print(f"%s, you have {shot_count} missles." % attacking_player.name)
        missle_location = attacking_player.moves(defending_board)

        hit_battleship = defending_board.shoot(missle_location)
        if hit_battleship is None:
            events("miss", {"Player": attacking_player.name})
            shot_count -= 1

        else:
            if hit_battleship.is_sunk():
                events("ship_sunk", {"Player": attacking_player.name})
                ship_sunk += 1
            else:
                events("ship_hit", {"Player": attacking_player.name})
                shot_count -= 1
        draw_board(defending_board)

        if defending_board.is_game_over():
            events("game_over", {"Player": attacking_player.name})
            break

        attacking_index = defending_index

    # Define a loop for playing the game again

    answer = input("\nWould you like to play again? Y or N\n").lower()
    if answer == "n":
        print("Thank you for playing.")
        exit(0)
    else:
        print("Let's get back out there!")
