"""
SmartTicTacToe - AI-Powered Tic-Tac-Toe
-----------------------------------------
An unbeatable Tic-Tac-Toe game where the computer opponent uses the
Minimax algorithm (implemented from scratch, no external AI libraries).

Author: CodeOrbit Tech - AI Internship Project
"""

import random

# ---------------------------------------------------------
# CONSTANTS
# ---------------------------------------------------------

EMPTY = " "

# All 8 possible winning combinations (using 0-indexed board positions)
WIN_COMBINATIONS = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),   # rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),   # columns
    (0, 4, 8), (2, 4, 6),              # diagonals
]


# ---------------------------------------------------------
# DISPLAY FUNCTIONS
# ---------------------------------------------------------

def print_welcome():
    """Show the welcome banner."""
    print("=" * 33)
    print("        SMART TICTACTOE")
    print("=" * 33)
    print("An AI opponent powered by the Minimax algorithm.")
    print("The AI plays perfectly - the best you can do is draw!\n")


def display_board(board):
    """
    Print the board. Empty cells show their position number (1-9)
    so the player knows what to type; filled cells show X or O.
    """
    def cell(i):
        return board[i] if board[i] != EMPTY else str(i + 1)

    print()
    print(f"     {cell(0)} | {cell(1)} | {cell(2)}")
    print("    -----------")
    print(f"     {cell(3)} | {cell(4)} | {cell(5)}")
    print("    -----------")
    print(f"     {cell(6)} | {cell(7)} | {cell(8)}")
    print()


def print_result(board, human, computer):
    """Print the final outcome of the game."""
    if check_winner(board, human):
        print("🎉 Congratulations! You won!")
    elif check_winner(board, computer):
        print("🤖 SmartTicTacToe wins!")
        print("Better luck next time!")
    else:
        print("🤝 It's a draw!")
        print("Both players played well.")


# ---------------------------------------------------------
# GAME LOGIC FUNCTIONS
# ---------------------------------------------------------

def check_winner(board, player):
    """Return True if `player` has a winning combination on the board."""
    return any(
        all(board[i] == player for i in combo)
        for combo in WIN_COMBINATIONS
    )


def is_board_full(board):
    """Return True if there are no empty cells left."""
    return EMPTY not in board


def get_available_moves(board):
    """Return a list of indices (0-8) for all empty cells."""
    return [i for i, value in enumerate(board) if value == EMPTY]


# ---------------------------------------------------------
# MINIMAX AI
# ---------------------------------------------------------

def minimax(board, is_maximizing, computer, human):
    """
    Recursively evaluate the board and return a score from the
    computer's perspective.

    Score meaning:
        +1  -> computer wins in this branch
        -1  -> human wins in this branch
         0  -> draw

    is_maximizing = True  -> it's the computer's (maximizing) turn
    is_maximizing = False -> it's the human's (minimizing) turn,
                              simulated as if the human always
                              plays their best possible move.
    """
    # --- Terminal states: stop recursing and score the board ---
    if check_winner(board, computer):
        return 1
    if check_winner(board, human):
        return -1
    if is_board_full(board):
        return 0

    # --- Recursive case: try every available move ---
    if is_maximizing:
        best_score = -float("inf")
        for move in get_available_moves(board):
            board[move] = computer                     # simulate move
            score = minimax(board, False, computer, human)
            board[move] = EMPTY                          # undo move
            best_score = max(best_score, score)
        return best_score
    else:
        best_score = float("inf")
        for move in get_available_moves(board):
            board[move] = human                          # simulate move
            score = minimax(board, True, computer, human)
            board[move] = EMPTY                            # undo move
            best_score = min(best_score, score)
        return best_score


def get_best_move(board, computer, human):
    """
    Try every available move, score each one using minimax,
    and return the index of the move with the best score for
    the computer.
    """
    best_score = -float("inf")
    best_moves = []

    for move in get_available_moves(board):
        board[move] = computer
        score = minimax(board, False, computer, human)
        board[move] = EMPTY

        if score > best_score:
            best_score = score
            best_moves = [move]
        elif score == best_score:
            best_moves.append(move)

    # If multiple moves are equally good, pick randomly among them
    # so the AI doesn't always play the exact same opening move.
    return random.choice(best_moves)


# ---------------------------------------------------------
# TURN FUNCTIONS
# ---------------------------------------------------------

def player_move(board, human):
    """Ask the human for a move, validate it, and apply it to the board."""
    while True:
        raw = input("Enter your move (1-9) or Q to Quit: ").strip().upper()
        
        if raw == "Q":
            print("\nThanks for playing SmartTicTacToe. Goodbye! 👋")
            exit()
    
        if not raw.isdigit():
            print("Please enter a number from 1 to 9.")
            continue

        position = int(raw)

        if position < 1 or position > 9:
            print("Invalid move. Please choose a position between 1 and 9.")
            continue

        index = position - 1
        if board[index] != EMPTY:
            print("Position already occupied. Choose an empty position.")
            continue

        board[index] = human
        return


def computer_move(board, computer, human):
    """Let the AI choose and play its move using minimax."""
    print("SmartTicTacToe is thinking...")
    move = get_best_move(board, computer, human)
    board[move] = computer
    print(f"Computer chooses position {move + 1}.")


# ---------------------------------------------------------
# GAME CONTROLLER
# ---------------------------------------------------------

def choose_symbol():
    """Ask the human which symbol they want to play as."""
    while True:
        choice = input("Choose your symbol - X or O (X goes first) and Q to Quit: ").strip().upper()
        if choice == "Q":
            print("\nSee you Nextime at SmartTicTacToe. Goodbye! 👋")
            exit()
        if choice in ("X", "O"):
            return choice
        print("Please enter X or O.")


def play_round(human, computer):
    """Play a single full game (round) and return the winner symbol or None."""
    board = [EMPTY] * 9
    # X always moves first, regardless of who is human/computer.
    current_turn = "X"

    display_board(board)

    while True:
        if current_turn == human:
            player_move(board, human)
        else:
            computer_move(board, computer, human)

        display_board(board)

        if check_winner(board, human) or check_winner(board, computer) or is_board_full(board):
            print_result(board, human, computer)
            if check_winner(board, human):
                return human
            elif check_winner(board, computer):
                return computer
            else:
                return None

        current_turn = "O" if current_turn == "X" else "X"


def play_game():
    """Main entry point: handles setup, replay loop, and the scoreboard."""
    print_welcome()

    human = choose_symbol()
    computer = "O" if human == "X" else "X"

    scoreboard = {"human": 0, "ai": 0, "draws": 0}

    while True:
        winner = play_round(human, computer)

        if winner == human:
            scoreboard["human"] += 1
        elif winner == computer:
            scoreboard["ai"] += 1
        else:
            scoreboard["draws"] += 1

        print("--- Scoreboard ---")
        print(f"Human Wins: {scoreboard['human']}")
        print(f"AI Wins:    {scoreboard['ai']}")
        print(f"Draws:      {scoreboard['draws']}")
        print("------------------\n")

        again = input("Would you like to play again? (y/n): ").strip().lower()
        if again != "y":
            print("\nThanks for playing SmartTicTacToe. Goodbye! 👋")
            break


if __name__ == "__main__":
    play_game()
