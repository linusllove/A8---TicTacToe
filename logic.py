# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable.

import random

class TicTacToeGame:
    def __init__(self, player1, player2):
        self.board = [[None, None, None] for _ in range(3)]
        self.current_player = player1
        self.other_player = player2

    def play_turn(self):
        x, y = self.current_player.make_move(self.board)

        if self.board[x][y] is not None:
            raise ValueError(f"The spot ({x}, {y}) is already taken.")

        self.board[x][y] = self.current_player.marker
        self.current_player, self.other_player = self.other_player, self.current_player

    def get_winner(self):
        for row in self.board:
            if row[0] == row[1] == row[2] and row[0] is not None:
                return row[0]

        for i in range(3):
            if self.board[0][i] == self.board[1][i] == self.board[2][i] and self.board[0][i] is not None:
                return self.board[0][i]

        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] is not None:
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] is not None:
            return self.board[0][2]

        return None

    def is_draw(self):
        return all(all(cell is not None for cell in row) for row in self.board)

class Player:
    def __init__(self, marker):
        self.marker = marker

    def make_move(self, board):
        x, y = map(int, input(f"Enter the position of (x,y) for {self.marker}, split with comma: ").split(","))
        return x, y

class Bot(Player):
    def make_move(self, board):
        empty_spots = [(x, y) for x in range(3) for y in range(3) if board[x][y] is None]
        return random.choice(empty_spots) if empty_spots else (0, 0)

def print_board(board):
    print("  0 1 2")
    for i, row in enumerate(board):
        print_row = [cell if cell is not None else ' ' for cell in row]
        print(f"{i} {' '.join(print_row)}")

def main():
    player1 = Player('X')
    player2 = Bot('O')
    game = TicTacToeGame(player1, player2)

    while True:
        print_board(game.board)
        game.play_turn()
        winner = game.get_winner()
        if winner:
            print_board(game.board)
            print(f"Player {winner} wins!")
            break
        if game.is_draw():
            print_board(game.board)
            print("It's a draw!")
            break

if __name__ == '__main__':
    main()

import random
import csv
import os

class TicTacToeGame:
    def __init__(self, player1, player2, database_file):
        self.board = [[None, None, None] for _ in range(3)]
        self.current_player = player1
        self.other_player = player2
        self.database_file = database_file

    def play_turn(self):
        x, y = self.current_player.make_move(self.board)

        if self.board[x][y] is not None:
            raise ValueError(f"The spot ({x}, {y}) is already taken.")

        self.board[x][y] = self.current_player.marker
        self.current_player, self.other_player = self.other_player, self.current_player

    def get_winner(self):
        for row in self.board:
            if row[0] == row[1] == row[2] and row[0] is not None:
                return row[0]

        for i in range(3):
            if self.board[0][i] == self.board[1][i] == self.board[2][i] and self.board[0][i] is not None:
                return self.board[0][i]

        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] is not None:
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] is not None:
            return self.board[0][2]

        return None

    def is_draw(self):
        return all(all(cell is not None for cell in row) for row in self.board)

    def record_winner(self, winner):
        if winner:
            with open(self.database_file, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([winner])

class Player:
    def __init__(self, marker):
        self.marker = marker

    def make_move(self, board):
        x, y = map(int, input(f"Enter the position of (x,y) for {self.marker}, split with comma: ").split(","))
        return x, y

class Bot(Player):
    def make_move(self, board):
        empty_spots = [(x, y) for x in range(3) for y in range(3) if board[x][y] is None]
        return random.choice(empty_spots) if empty_spots else (0, 0)

def print_board_to_file(board, file):
    with open(file, 'a') as f:
        f.write("  0 1 2\n")
        for i, row in enumerate(board):
            print_row = [cell if cell is not None else ' ' for cell in row]
            f.write(f"{i} {' '.join(print_row)}\n")

def main():
    logs_directory = './logs'
    os.makedirs(logs_directory, exist_ok=True)
    database_file = os.path.join(logs_directory, 'winners.csv')
    board_file = os.path.join(logs_directory, 'game_board.txt')

    player1 = Player('X')
    player2 = Bot('O')
    game = TicTacToeGame(player1, player2, database_file)

    while True:
        print_board_to_file(game.board, board_file)
        game.play_turn()
        winner = game.get_winner()
        if winner:
            game.record_winner(winner)
            print_board_to_file(game.board, board_file)
            with open(board_file, 'a') as f:
                f.write(f"Player {winner} wins!\n")
            break
        if game.is_draw():
            print_board_to_file(game.board, board_file)
            with open(board_file, 'a') as f:
                f.write("It's a draw!\n")
            break

if __name__ == '__main__':
    main()

