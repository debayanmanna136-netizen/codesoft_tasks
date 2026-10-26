"""
╔══════════════════════════════════════════════════════════════╗
║          TIC-TAC-TOE — AI vs Human (Python CLI)             ║
║        CODSOFT AI Internship | Task 2                       ║
║                                                              ║
║  Algorithm: Minimax with Alpha-Beta Pruning                  ║
║  The AI is mathematically unbeatable on Hard difficulty.     ║
╚══════════════════════════════════════════════════════════════╝
"""

import sys
import os
import math
import random
import time


# ──────────────────────────────────────────────
#  ANSI Color Codes (terminal styling)
# ──────────────────────────────────────────────
class Color:
    RESET   = "\033[0m"
    BOLD    = "\033[1m"
    DIM     = "\033[2m"
    RED     = "\033[91m"
    GREEN   = "\033[92m"
    YELLOW  = "\033[93m"
    BLUE    = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN    = "\033[96m"
    WHITE   = "\033[97m"
    GRAY    = "\033[90m"

    X_COLOR = "\033[96m"   # Cyan for X (Human)
    O_COLOR = "\033[95m"   # Magenta for O (AI)
    WIN_COLOR = "\033[92m" # Green for winning cells


def colored(text: str, *codes: str) -> str:
    """Wrap text with ANSI color codes."""
    return "".join(codes) + str(text) + Color.RESET


def clear():
    """Clear the terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")


# ──────────────────────────────────────────────
#  Board Constants & Helpers
# ──────────────────────────────────────────────
HUMAN = "X"
AI    = "O"
EMPTY = " "

WIN_LINES = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),   # rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),   # columns
    (0, 4, 8), (2, 4, 6),              # diagonals
]


def new_board() -> list:
    """Return a fresh 3×3 board (list of 9 elements)."""
    return [EMPTY] * 9


def check_winner(board: list) -> str | None:
    """Return 'X', 'O', or None if no winner yet."""
    for a, b, c in WIN_LINES:
        if board[a] != EMPTY and board[a] == board[b] == board[c]:
            return board[a]
    return None


def get_win_line(board: list) -> tuple | None:
    """Return the winning triple of indices, or None."""
    for line in WIN_LINES:
        a, b, c = line
        if board[a] != EMPTY and board[a] == board[b] == board[c]:
            return line
    return None


def is_full(board: list) -> bool:
    """Return True when no EMPTY cells remain."""
    return EMPTY not in board


def get_empty(board: list) -> list:
    """Return list of empty cell indices."""
    return [i for i, v in enumerate(board) if v == EMPTY]


def is_terminal(board: list) -> bool:
    """Return True if the game is over (win or draw)."""
    return check_winner(board) is not None or is_full(board)


# ──────────────────────────────────────────────
#  Minimax with Alpha-Beta Pruning
# ──────────────────────────────────────────────
def minimax(board: list, depth: int, is_maximizing: bool,
            alpha: float, beta: float) -> dict:
    """
    Minimax algorithm with Alpha-Beta Pruning.

    Parameters
    ----------
    board          : current board state (list of 9 cells)
    depth          : current search depth (used to prefer faster wins)
    is_maximizing  : True → AI's turn (maximize score)
                     False → Human's turn (minimize score)
    alpha          : best score already secured for maximizer
    beta           : best score already secured for minimizer

    Returns
    -------
    dict with keys:
        'score' : heuristic value of the board
        'index' : best cell index for current player (only at top level)

    Scoring convention
    ------------------
    +10 – depth  →  AI wins sooner = better
    -10 + depth  →  Human wins sooner = worse for AI
     0           →  draw
    """
    winner = check_winner(board)
    if winner == AI:
        return {"score":  10 - depth}
    if winner == HUMAN:
        return {"score": -10 + depth}
    if is_full(board):
        return {"score": 0}

    best_index = None

    if is_maximizing:
        best_score = -math.inf
        for i in get_empty(board):
            board[i] = AI
            result = minimax(board, depth + 1, False, alpha, beta)
            board[i] = EMPTY
            if result["score"] > best_score:
                best_score = result["score"]
                best_index = i
            alpha = max(alpha, best_score)
            if beta <= alpha:          # Beta cutoff — prune remaining branches
                break
        return {"score": best_score, "index": best_index}

    else:
        best_score = math.inf
        for i in get_empty(board):
            board[i] = HUMAN
            result = minimax(board, depth + 1, True, alpha, beta)
            board[i] = EMPTY
            if result["score"] < best_score:
                best_score = result["score"]
                best_index = i
            beta = min(beta, best_score)
            if beta <= alpha:          # Alpha cutoff — prune remaining branches
                break
        return {"score": best_score, "index": best_index}


# ──────────────────────────────────────────────
#  AI Move Selection
# ──────────────────────────────────────────────
def ai_move(board: list, difficulty: str) -> int:
    """
    Choose AI's next cell based on difficulty.

    Easy   → random cell
    Medium → 50% random, 50% optimal
    Hard   → always optimal (unbeatable)
    """
    empties = get_empty(board)

    if difficulty == "easy":
        return random.choice(empties)

    if difficulty == "medium":
        if random.random() < 0.5:
            return random.choice(empties)
        # fall through to hard

    # Hard: full Minimax + Alpha-Beta Pruning
    result = minimax(board, 0, True, -math.inf, math.inf)
    return result["index"]


# ──────────────────────────────────────────────
#  Board Rendering
# ──────────────────────────────────────────────
def render_board(board: list, win_line: tuple | None = None) -> None:
    """Pretty-print the board with colors and position hints."""
    symbols = {}
    for i, val in enumerate(board):
        if val == HUMAN:
            if win_line and i in win_line:
                symbols[i] = colored(val, Color.BOLD, Color.WIN_COLOR)
            else:
                symbols[i] = colored(val, Color.BOLD, Color.X_COLOR)
        elif val == AI:
            if win_line and i in win_line:
                symbols[i] = colored(val, Color.BOLD, Color.WIN_COLOR)
            else:
                symbols[i] = colored(val, Color.BOLD, Color.O_COLOR)
        else:
            symbols[i] = colored(str(i + 1), Color.DIM, Color.GRAY)

    sep = colored("─────────────", Color.DIM, Color.GRAY)

    print()
    print(f"  {symbols[0]} │ {symbols[1]} │ {symbols[2]}")
    print(f" {sep}")
    print(f"  {symbols[3]} │ {symbols[4]} │ {symbols[5]}")
    print(f" {sep}")
    print(f"  {symbols[6]} │ {symbols[7]} │ {symbols[8]}")
    print()


# ──────────────────────────────────────────────
#  UI Helpers
# ──────────────────────────────────────────────
BANNER = f"""
{colored("╔══════════════════════════════════════════╗", Color.CYAN, Color.BOLD)}
{colored("║", Color.CYAN, Color.BOLD)}   {colored("TIC-TAC-TOE  ·  AI vs Human", Color.WHITE, Color.BOLD)}         {colored("║", Color.CYAN, Color.BOLD)}
{colored("║", Color.CYAN, Color.BOLD)}   {colored("Minimax + Alpha-Beta Pruning", Color.GRAY)}         {colored("║", Color.CYAN, Color.BOLD)}
{colored("╚══════════════════════════════════════════╝", Color.CYAN, Color.BOLD)}
"""


def print_banner():
    print(BANNER)


def print_scores(scores: dict):
    x_str = colored(f"X: {scores['X']}", Color.BOLD, Color.X_COLOR)
    o_str = colored(f"O: {scores['O']}", Color.BOLD, Color.O_COLOR)
    d_str = colored(f"Draws: {scores['draw']}", Color.GRAY)
    print(f"  {x_str}   {o_str}   {d_str}")


def prompt_difficulty() -> str:
    print(f"\n  Select difficulty:")
    print(f"    {colored('1', Color.YELLOW)} → Easy  (random AI)")
    print(f"    {colored('2', Color.YELLOW)} → Medium (mixed strategy)")
    print(f"    {colored('3', Color.YELLOW)} → Hard  (unbeatable AI)")
    while True:
        choice = input(f"\n  {colored('Enter choice [1-3]:', Color.CYAN)} ").strip()
        if choice == "1": return "easy"
        if choice == "2": return "medium"
        if choice == "3": return "hard"
        print(colored("  ⚠  Please enter 1, 2, or 3.", Color.RED))


def prompt_mode() -> str:
    print(f"\n  Select game mode:")
    print(f"    {colored('1', Color.YELLOW)} → vs AI")
    print(f"    {colored('2', Color.YELLOW)} → 2 Players (local)")
    while True:
        choice = input(f"\n  {colored('Enter choice [1-2]:', Color.CYAN)} ").strip()
        if choice == "1": return "ai"
        if choice == "2": return "2p"
        print(colored("  ⚠  Please enter 1 or 2.", Color.RED))


def prompt_move(board: list, player: str) -> int:
    """Ask the current player for their cell (1-9)."""
    label = colored(f"[{player}]", Color.X_COLOR if player == HUMAN else Color.O_COLOR, Color.BOLD)
    while True:
        raw = input(f"  {label} {colored('Enter cell (1-9):', Color.CYAN)} ").strip()
        if raw.lower() in ("q", "quit", "exit"):
            print(colored("\n  Thanks for playing! Goodbye.\n", Color.GRAY))
            sys.exit(0)
        try:
            idx = int(raw) - 1
            if 0 <= idx <= 8 and board[idx] == EMPTY:
                return idx
            print(colored("  ⚠  Cell is invalid or already taken. Try again.", Color.RED))
        except ValueError:
            print(colored("  ⚠  Please enter a number between 1 and 9.", Color.RED))


# ──────────────────────────────────────────────
#  Main Game Loop
# ──────────────────────────────────────────────
def play_game(mode: str, difficulty: str, scores: dict) -> None:
    """Run a single game round."""
    board = new_board()
    current = HUMAN      # X always goes first
    game_over = False

    while not game_over:
        clear()
        print_banner()
        print_scores(scores)
        diff_label = colored(f"[{difficulty.upper()}]", Color.YELLOW)
        mode_label = colored(f"[{'vs AI' if mode == 'ai' else '2 Players'}]", Color.CYAN)
        print(f"  {mode_label}  {diff_label}\n")
        render_board(board)

        # ── Determine whose move it is ──────────────────────
        if mode == "ai" and current == AI:
            print(colored("  🤖 AI is thinking…", Color.O_COLOR))
            time.sleep(0.4)
            idx = ai_move(board, difficulty)
            board[idx] = AI
        else:
            # Human input
            if mode == "ai":
                print(colored("  Your turn (X). Type 'q' to quit.", Color.X_COLOR))
            else:
                p_color = Color.X_COLOR if current == HUMAN else Color.O_COLOR
                print(colored(f"  Player {current}'s turn. Type 'q' to quit.", p_color))
            idx = prompt_move(board, current)
            board[idx] = current

        # ── Check game outcome ──────────────────────────────
        winner   = check_winner(board)
        win_line = get_win_line(board)
        draw     = is_full(board) and winner is None

        if winner or draw:
            clear()
            print_banner()
            render_board(board, win_line)
            game_over = True

            if winner == HUMAN:
                scores["X"] += 1
                msg = colored("  🎉 You win! Congratulations!", Color.WIN_COLOR, Color.BOLD)
            elif winner == AI:
                scores["O"] += 1
                msg = colored("  🤖 AI wins! Better luck next time.", Color.O_COLOR, Color.BOLD)
            else:
                scores["draw"] += 1
                msg = colored("  🤝 It's a draw! Well played.", Color.YELLOW, Color.BOLD)

            print(msg)
            print_scores(scores)
        else:
            # Alternate turns
            current = AI if current == HUMAN else HUMAN


def main():
    """Entry point — settings selection then repeated game loop."""
    clear()
    print_banner()

    mode       = prompt_mode()
    difficulty = prompt_difficulty() if mode == "ai" else "hard"
    scores     = {"X": 0, "O": 0, "draw": 0}

    while True:
        play_game(mode, difficulty, scores)

        print()
        again = input(colored("  Play again? [y/n]: ", Color.CYAN)).strip().lower()
        if again not in ("y", "yes"):
            print(colored("\n  Thanks for playing! Final scores:", Color.GRAY))
            print_scores(scores)
            print()
            break

        # Optional: change difficulty between rounds
        change = input(colored("  Change settings? [y/n]: ", Color.CYAN)).strip().lower()
        if change in ("y", "yes"):
            clear()
            print_banner()
            mode       = prompt_mode()
            difficulty = prompt_difficulty() if mode == "ai" else "hard"


if __name__ == "__main__":
    main()
