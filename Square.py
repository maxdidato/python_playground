import random


class Square:

    def __init__(self, position):
        self._position = position

    def action(self, player):
        player.set_current_position(self._position)
        print(f"Player {player.get_name()} is on position {self._position}")

class Goal(Square):
    def action(self,player):
        Square.action(self, player)
        print(f"YUHUUUUUUU, PLAYER {player.get_name()} WON THE GAME!!!!!!!!!")

class Snake(Square):

    def __init__(self, position, action_position):
        super().__init__(position)
        self._action_position = action_position

    def action(self, player):
        Square.action(self, player)
        print(f"AH HA! It is a SNAKE square. Player {player.get_name()} pushed back to {self._action_position}")
        player.set_current_position(self._action_position)

class JumpTurn(Square):
    def action(self,player):
        Square.action(self, player)
        player.jump_turn = True
        print(f"Player {player.get_name()} jump next turn !!!!!! ")


class Ladder(Square):
    def __init__(self, position, action_position):
        super().__init__(position)
        self._action_position = action_position

    def action(self, player):
        Square.action(self, player)
        print(f"GOOD!! It is a LADDER square. Player {player.get_name()} pushed forward to {self._action_position}")
        player.set_current_position(self._action_position)

class Player:
    def __init__(self,name):
        self._name = name
        self._position = 1
        self.jump_turn = False
        print(f"Hi, I am player {self._name}")

    def get_name(self):
        return str(self._name).capitalize()

    def set_current_position(self,position):
        self._position = position

    def current_position(self):
        return self._position

    def roll_dice(self):
        dice = (random.randint(1,6),random.randint(1,6))
        print(f"{self._name}  rolled {dice[0]} and {dice[1]}")
        return dice

    def has_won(self):
        return self._position == 100


class Squares(list):
    def __getitem__(self, y):
        return list.__getitem__(self,y-1)


class Board:
    NUM_OF_SQUARES = 100

    def __init__(self):
        self._players = self.initialize_players()
        self.squares = Squares()
        self.generate_board()
        self.current_player = self._players[0]
        print(f"{self.current_player.get_name()} will begin")

    def start_game(self):
        while not self._players[0].has_won() and not self._players[1].has_won():
            dice_rolled = self.current_player.roll_dice()
            self.squares[self.move_next_square(dice_rolled)].action(self.current_player)
            if dice_rolled[0] == dice_rolled[1]:
                print(f"How lucky {self.current_player.get_name()}, roll the dice again")
            else:
                self.switch_turn()
            # while input("PRESS ENTER TO PLAY"):
            #     pass

    def move_next_square(self, dice_rolled):
        next_square = self.current_player.current_position() + sum(dice_rolled)
        if next_square > Board.NUM_OF_SQUARES:
            next_square = self.end_of_the_board(next_square)
        return next_square

    def end_of_the_board(self, next_square):
        return Board.NUM_OF_SQUARES - (next_square - Board.NUM_OF_SQUARES)

    def switch_turn(self):
        self.current_player = self._players[(self._players.index(self.current_player) + 1) % len(self._players)]
        if self.current_player.jump_turn:
            print(f"Player {self.current_player.get_name()} will jump this turn! ")
            self.current_player.jump_turn = False
            self.current_player = self._players[(self._players.index(self.current_player) + 1) % len(self._players)]
            print(f"Player {self.current_player.get_name()} can roll the dice again")



    def initialize_players(self):
        name = input("Name of Player 1: ")
        player1 = Player(name)
        name = input("Name of Player 2: ")
        player2 = Player(name)
        return player1, player2

    def generate_board(self):

        for i in range(1, Board.NUM_OF_SQUARES+1):
            self.squares.append(Square(i))
        self.squares[1] = Ladder(2, 38)
        self.squares[3] = Ladder(4, 14)
        self.squares[8] = Ladder(9, 31)
        self.squares[9] = JumpTurn(10)
        self.squares[32] = Ladder(33, 85)
        self.squares[51] = Ladder(52, 88)
        self.squares[52] = JumpTurn(53)
        self.squares[79] = Ladder(80, 99)
        self.squares[97] = Snake(98, 8)
        self.squares[91] = Snake(92, 53)
        self.squares[50] = Snake(51, 11)
        self.squares[55] = Snake(56, 15)
        self.squares[65] = JumpTurn(66)
        self.squares[61] = Snake(62, 57)
        self.squares[99] = Goal(100)


new_board = Board()
new_board.start_game()

