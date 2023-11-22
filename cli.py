# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import TicTacToeGame, HumanPlayer, BotPlayer

def print_game_board(board):
    print("  0 1 2")
    for i, row in enumerate(board):
        print_row = [cell if cell is not None else ' ' for cell in row]
        print(f"{i} {' '.join(print_row)}")

def main():
    mode = input("Choose mode (1 for single player, 2 for two players): ")
    player1 = HumanPlayer('X')
    player2 = BotPlayer('O') if mode == '1' else HumanPlayer('O')

    game = TicTacToeGame(player1, player2)

    while True:
        print_game_board(game.get_board())
        game.play_turn()
        winner = game.get_winner()
        if winner:
            print_game_board(game.get_board())
            print(f"Player {winner} wins!")
            break
        if game.is_draw():
            print_game_board(game.get_board())
            print("It's a draw!")
            break

if __name__ == '__main__':
    main()
