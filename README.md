# Console-Based Strategy Game (X/O Duel)

This is a console-based Python game where two players (or one player and the computer) compete by placing X and O pieces on a customizable board. Each player has unique placement rules, and the game ends when no more valid moves are possible.

## Features

- Player vs Player and Player vs Computer modes
- Customizable board size (minimum 4x4)
- Basic AI with Minimax algorithm for computer opponent
- Move validation and automatic board display after each turn
- Evaluation function for game state estimation

## Game Rules

- The board consists of cells, each starting as `None`.
- Player **X** (0) places their piece in two vertically stacked cells.
- Player **O** (1) places their piece in two horizontally adjacent cells.
- A move is invalid if:
  - It goes outside the board.
  - It overlaps with another piece.
- The game ends when no valid moves are left for the current player.

## How to Run

1. Clone the repository or copy the code into a `.py` file:
    ```bash
    python game.py
    ```

2. Follow the prompts:
    - Enter board dimensions (minimum 4x4).
    - Choose the first player (`0` for X, `1` for O).
    - Choose game mode: `0` for PvP or `1` for PvC.

## AI Strategy

The computer opponent uses a basic **Minimax** strategy with depth-limited search to evaluate and select optimal moves. The evaluation function is designed to assess available valid moves for both X and O and estimate the board state accordingly.

## Project Structure

- `startGame()` — Entry point for setting up the game.
- `provera()` — Validates if a move is within bounds and allowed.
- `Upisi()` — Handles move input and updates the board.
- `CovekProtivRacunara()` — Handles gameplay against AI.
- `max_value()` / `min_value()` — Core of the Minimax algorithm.
- `showTable()` — Prints the current state of the board.

## Limitations

- No GUI; purely console-based.
- Basic AI; not optimized for high-level play.
- No save/load feature for game state.

## Requirements

- Python 3.x
- No external libraries required

## Author

Made with logic and Python. Designed to demonstrate strategic thinking and algorithm design.
Teodora Zlatanovic
Computer Science graduate specializing in software development, based in Serbia.
GitHub: github.com/TeodoraZ98



