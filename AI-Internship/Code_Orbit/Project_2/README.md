# SmartTicTacToe — AI-Powered Tic-Tac-Toe

## Overview

SmartTicTacToe is a classic 3×3 Tic-Tac-Toe game played in the terminal. One player is human, the other is the computer. The computer's moves are chosen using the **Minimax algorithm**, a decision-making technique from classical AI/game theory that recursively explores all possible future game states to find the guaranteed-best move.

## Objective

This project demonstrates how a simple, well-understood algorithm — with no neural networks, no training data, and no external AI services — can produce genuinely intelligent, optimal decision-making in a game environment.

## Features

- Human vs Computer gameplay
- AI opponent powered by the Minimax algorithm
- Standard 3×3 game board
- Full input validation (non-numeric input, out-of-range input, occupied cells)
- Programmatic win, loss, and draw detection
- Replay option after each game
- Clear, readable board display after every move
- Simple scoreboard tracking wins/losses/draws across a session

## Technologies

- Python 3
- Minimax Algorithm
- Recursion
- Conditional Logic
- Functions
- Lists

No databases, no web scraping, no ML/DL libraries, and no external generative AI APIs are used anywhere in this project.

## How Minimax Works

Minimax works by having the AI **imagine every possible way the rest of the game could unfold**, then choosing the move that leads to its best guaranteed outcome, assuming the human always plays optimally too.

- **Maximizing player** — the computer. It wants the highest score, so it looks for the move that leads to the best result for itself.
- **Minimizing player** — the human, simulated by the AI as always making the move that is *worst* for the computer.
- **Game state** — a snapshot of the board at any given moment.
- **Terminal state** — a finished game (win, loss, or draw), where recursion stops and a score is assigned.
- **Score** — `+1` if the computer wins that branch, `-1` if the human wins, `0` for a draw.
- **Recursion** — the algorithm calls itself on the resulting board after each hypothetical move, diving deeper into future turns until it reaches a terminal state. Those scores then bubble back up the call stack, with the computer picking the maximum score at its turns and the (simulated) human picking the minimum at theirs.

Because a 3×3 Tic-Tac-Toe board is small, Minimax can explore the entire game tree on every single turn. This is why the AI plays perfectly — it can never be beaten, only drawn against with best play.

### Diagram

```
Current Board
     ↓
AI considers possible moves
     ↓
Each move creates a possible future board
     ↓
AI considers the opponent's possible response
     ↓
Continue until a terminal state
     ↓
Evaluate: Win = +1   Draw = 0   Loss = -1
     ↓
Choose the best move
```

## Game Flow

```
START
  ↓
Welcome Screen
  ↓
Choose Player Symbol
  ↓
Display Empty Board
  ↓
Human Move → Display Board → Check Win/Draw
  ↓ (if not over)
Computer Move (Minimax) → Display Board → Check Win/Draw
  ↓ (repeat until game over)
Display Result
  ↓
Play Again? (y/n)
```

## Project Structure

```
CodeOrbit_SmartTicTacToe/
│
├── tic_tac_toe.py
├── README.md
└── screenshots/
    └── game_demo.png
```

## How to Run

Requires Python 3.

```bash
python tic_tac_toe.py
```

## Example Gameplay

```
=================================
        SMART TICTACTOE
=================================
An AI opponent powered by the Minimax algorithm.
The AI plays perfectly - the best you can do is draw!

Choose your symbol - X or O (X goes first): X

     1 | 2 | 3
    -----------
     4 | 5 | 6
    -----------
     7 | 8 | 9

Enter your move (1-9): 5

     1 | 2 | 3
    -----------
     4 | X | 6
    -----------
     7 | 8 | 9

SmartTicTacToe is thinking...
Computer chooses position 1.

     O | 2 | 3
    -----------
     4 | X | 6
    -----------
     7 | 8 | 9

Enter your move (1-9): 9
...
🤝 It's a draw!
Both players played well.
--- Scoreboard ---
Human Wins: 0
AI Wins:    0
Draws:      1
------------------

Would you like to play again? (y/n):
```

## Testing

The project was manually and automatically tested for:

- Human win, computer win, and draw outcomes
- Invalid input handling (non-numeric input, out-of-range numbers, occupied cells)
- The AI correctly blocking an imminent human win
- The AI correctly taking an available winning move
- The replay loop (`y` and `n` paths)
- An automated 500-game simulation against random human moves, confirming the AI never loses (only wins or draws)


## Limitations

- The game is limited to a standard 3×3 board.
- The AI is designed specifically for this game; it is not a general-purpose AI system.
- Minimax becomes computationally expensive on much larger game spaces (e.g., a 5×5 or larger board would require significant optimization, such as alpha-beta pruning).

## Future Improvements

- Graphical user interface (GUI)
- Selectable difficulty levels (e.g., an intentionally imperfect "easy" mode)
- Support for larger boards
- Sound effects
- Local multiplayer mode (human vs human)
- Web-based version


## Internship Context

This project was developed as part of the **CodeOrbit Tech Artificial Intelligence Internship** (1-Month Program), fulfilling the "Tic-Tac-Toe with Simple AI" task requirement to build a Tic-Tac-Toe game with an AI opponent using the Minimax algorithm.
