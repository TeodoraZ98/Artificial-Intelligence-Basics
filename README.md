```markdown
# Artificial Intelligence Basics

This project is a simple turn-based strategic game implemented in Python that simulates a grid-based board game between two players (X and O). It also features a basic AI using the Minimax algorithm with alpha-beta pruning for the computer opponent. The game includes rule validation, board visualization, and gameplay between human vs. human or human vs. computer.

## Project Highlights

- Grid-based board game engine
- Human vs Human or Human vs Computer gameplay
- AI opponent with Minimax and alpha-beta pruning
- Move validation and input handling
- Dynamic board rendering in the terminal

## Game Rules

- The board is a grid defined by user input (minimum 4x4).
- Player X places tiles vertically, occupying two rows in the same column.
- Player O places tiles horizontally, occupying two columns in the same row.
- The game alternates turns between players until no legal moves remain.

## Features

- Input validation to prevent moves outside the board or on occupied cells
- Automatic turn switching and board updates
- Victory check and game-end detection
- AI decision-making up to 3 levels of depth
- Console-based board display for intuitive tracking

## How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/TeodoraZ98/Artificial-Intelligence-Basics.git
   cd Artificial-Intelligence-Basics
   ```

2. Run the game:

   ```bash
   python game.py
   ```

   *(Make sure the code is saved in a file like `game.py`.)*

3. Follow the prompts in the terminal to select board size, players, and start playing.

## Technologies Used

- Python 3
- Standard Python libraries (no external dependencies)

## Potential Improvements

- GUI using Tkinter or Pygame
- Adjustable AI difficulty levels
- Multiplayer over network
- Enhanced evaluation functions for AI scoring

## Author

Teodora Zlatanovic  
Computer Science graduate focused on software development and artificial intelligence.  
GitHub: [github.com/TeodoraZ98](https://github.com/TeodoraZ98)
```


