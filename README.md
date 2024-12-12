# Tic Tac Toe Game

THIS IS THE NEWEST VERSION OF: https://github.com/sorflow/tic-tac-toe
This project is a Python implementation of the classic Tic Tac Toe game. Players can compete against a computer opponent, which uses basic AI strategies to either block the player or attempt to win. The game supports an interactive console-based experience.

## Features

- **Single-player mode:** Play against the computer.
- **AI Opponent:** The computer attempts to win or block the player strategically.
- **Dynamic Gameplay:** The player can make moves by entering row and column indices.
- **Clear Feedback:** The board is updated after every move, and the game's result is announced.

## How to Run

1. Ensure you have Python installed on your machine (Python 3.6 or higher is recommended).
2. Download or clone the repository containing the game script.
3. Open a terminal or command prompt and navigate to the folder containing the script.
4. Run the script by executing:
   ```
   python tictactoe.py
   ```
5. Enter your name when prompted, and start playing by entering row and column numbers (e.g., `1 2` for row 1, column 2).

## Rules

- The game is played on a 3x3 grid.
- Players take turns placing their marker (`X` for the player and `O` for the computer) in an empty cell.
- The first player to align three of their markers horizontally, vertically, or diagonally wins.
- If all cells are filled and no player has aligned three markers, the game ends in a draw.

## AI Strategy

The computer opponent uses the following approach:
1. **Winning Move:** If a winning move is available, the computer takes it.
2. **Blocking Move:** If the player is about to win, the computer blocks them.
3. **Random Move:** If neither a winning nor blocking move is available, the computer chooses a random empty cell.

## Example Gameplay

```
Enter your name: Alice
Welcome to Tic Tac Toe, Alice!
To play, enter the row and column number (e.g., '1 2' for row 1, column 2).

  0   1   2
0    |   |  
  -----------
1    |   |  
  -----------
2    |   |  

Alice's turn
Enter row and column (0, 1, 2) separated by a space: 1 1

  0   1   2
0    |   |  
  -----------
1    | X |  
  -----------
2    |   |  

Computer's turn

  0   1   2
0    |   |  
  -----------
1    | X | O
  -----------
2    |   |  
```

## Future Enhancements

- Implement a graphical user interface (GUI) for a more immersive experience.
- Add a two-player mode for local multiplayer.
- Improve AI to use minimax or other advanced algorithms for optimal gameplay.

## License

This project is released under the MIT License.

---

Enjoy playing Tic Tac Toe! If you have suggestions or feedback, feel free to contribute or open an issue.
