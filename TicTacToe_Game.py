
import random

class TicTacToe:
    def __init__(self, player_name):
        # Initialize a 3x3 board
        self.board = [[None for _ in range(3)] for _ in range(3)]
        self.player_name = player_name
        self.current_player = "X"

    def display_board(self):
        # Display the board with better formatting
        print("\n  0   1   2")
        for idx, row in enumerate(self.board):
            print(f"{idx} " + " | ".join([cell if cell else " " for cell in row]))
            if idx < 2:
                print("  " + "-" * 11)

    def is_valid_move(self, row, col):
        # Check if the move is within bounds and the cell is empty
        return 0 <= row < 3 and 0 <= col < 3 and self.board[row][col] is None

    def make_move(self, row, col):
        if self.is_valid_move(row, col):
            self.board[row][col] = self.current_player
            return True
        else:
            print("Invalid move. Please choose an empty cell within the grid.")
            return False

    def check_winner(self):
        # Check rows, columns, and diagonals for a win
        for i in range(3):
            # Check rows
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != None:
                return self.board[i][0]
            # Check columns
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != None:
                return self.board[0][i]

        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != None:
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != None:
            return self.board[0][2]

        return None

    def is_full(self):
        # Check if the board is full
        return all(cell is not None for row in self.board for cell in row)

    def switch_player(self):
        # Switch the current player
        self.current_player = "O" if self.current_player == "X" else "X"

    def computer_move(self):
        # Attempt to win or block the opponent
        for i in range(3):
            for j in range(3):
                if self.is_valid_move(i, j):
                    # Try to win
                    self.board[i][j] = "O"
                    if self.check_winner() == "O":
                        return (i, j)
                    self.board[i][j] = None

                    # Try to block
                    self.board[i][j] = "X"
                    if self.check_winner() == "X":
                        self.board[i][j] = None
                        return (i, j)
                    self.board[i][j] = None

        # Otherwise, pick a random valid move
        empty_cells = [(row, col) for row in range(3) for col in range(3) if self.board[row][col] is None]
        if empty_cells:
            return random.choice(empty_cells)
        return None

    def play_game(self):
        print(f"Welcome to Tic Tac Toe, {self.player_name}!")
        print("To play, enter the row and column number (e.g., '1 2' for row 1, column 2).\n")
        while True:
            self.display_board()
            if self.current_player == "X":
                print(f"{self.player_name}'s turn")
                try:
                    row, col = map(int, input("Enter row and column (0, 1, 2) separated by a space: ").split())
                    if self.make_move(row, col):
                        winner = self.check_winner()
                        if winner:
                            self.display_board()
                            print(f"Congratulations! {self.player_name} wins!" if winner == "X" else "Computer wins!")
                            break
                        elif self.is_full():
                            self.display_board()
                            print("It's a draw! Well played.")
                            break
                        self.switch_player()
                except ValueError:
                    print("Invalid input. Please enter two numbers separated by a space.")
            else:
                print("Computer's turn")
                move = self.computer_move()
                if move:
                    self.make_move(*move)
                    winner = self.check_winner()
                    if winner:
                        self.display_board()
                        print(f"Congratulations! {self.player_name} wins!" if winner == "X" else "Computer wins!")
                        break
                    elif self.is_full():
                        self.display_board()
                        print("It's a draw! Well played.")
                        break
                    self.switch_player()

if __name__ == "__main__":
    player_name = input("Enter your name: ")
    game = TicTacToe(player_name)
    game.play_game()
