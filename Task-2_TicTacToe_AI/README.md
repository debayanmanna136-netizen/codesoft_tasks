# Task 2 · Unbeatable Tic-Tac-Toe AI Agent

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![Algorithm](https://img.shields.io/badge/Algorithm-Minimax%20%2B%20Alpha--Beta-blueviolet?style=for-the-badge)

An intelligent, mathematically unbeatable Tic-Tac-Toe AI agent developed for the **CODSOFT AI Internship (Task 2)**. 

This project provides **two complete interfaces**:
1. 🐍 **Python CLI Game** (`tictactoe.py`) — Colorized terminal interface with ANSI styling.
2. 🌐 **Interactive Web Game** (`tictactoe.html`) — Modern glassmorphism UI with neon lighting, sound-free ripple effects, dynamic scoreboards, and instant responsiveness.

---

## 🧠 How the AI Works

### 1. Minimax Algorithm
Tic-Tac-Toe is a zero-sum, finite, perfect-information two-player game. The **Minimax** algorithm models all possible future board states from the current move:
- **AI (Maximizer)**: Chooses the move that maximizes the evaluation score.
- **Human (Minimizer)**: Assumed to play optimally to minimize the AI's score.

#### Scoring Function
$$\text{Score} = \begin{cases} +10 - \text{depth} & \text{if AI wins (earlier wins are prioritized)} \\ -10 + \text{depth} & \text{if Human wins (later losses are penalized less)} \\ 0 & \text{if Draw} \end{cases}$$

### 2. Alpha-Beta Pruning Optimization
In a standard Minimax search, every possible leaf in the game tree is visited ($O(b^d)$ nodes). **Alpha-Beta Pruning** significantly reduces the number of evaluated branches:
- **$\alpha$ (Alpha)**: The best value the maximizer is currently guaranteed.
- **$\beta$ (Beta)**: The best value the minimizer is currently guaranteed.
- **Pruning condition**: As soon as $\beta \le \alpha$, the remaining child nodes are pruned because the opponent would never allow that path to be reached.

| Metric | Pure Minimax | Minimax + Alpha-Beta |
|---|---|---|
| Search Tree Nodes | Up to $9! = 362,880$ (without symmetry) | **Cut by up to 60-70%** |
| Time Complexity | $\mathcal{O}(b^d)$ | $\mathcal{O}(b^{d/2})$ |
| Outcome | Unbeatable | **Identical optimal outcome, computed in milliseconds** |

---

## 🎮 Game Modes & Difficulty Levels

- **Difficulty Settings**:
  - 🟢 **Easy**: The AI picks random available cells.
  - 🟡 **Medium**: 50% random moves, 50% optimal Minimax moves.
  - 🔴 **Hard**: Full Minimax with Alpha-Beta pruning — **mathematically impossible to beat!**
- **Modes**:
  - 🤖 **Player vs AI**
  - 👥 **2-Player Local** (pass-and-play)

---

## 💻 How to Run

### Option A: Interactive Web App (Recommended)
Simply open `tictactoe.html` in any modern web browser (Google Chrome, Microsoft Edge, Firefox, Brave):
```bash
# On Windows, you can launch it directly from terminal:
start tictactoe.html
```

### Option B: Terminal CLI (Python)
No external libraries needed!
```bash
# Navigate to directory
cd Task-2_TicTacToe_AI

# Run the game
python tictactoe.py
```

---

## 📁 File Structure

```text
Task-2_TicTacToe_AI/
├── tictactoe.py       # Python CLI implementation with ANSI colors
├── tictactoe.html     # Full web application (HTML5, CSS3, Vanilla JS)
├── requirements.txt   # Dependencies info (Standard library only)
└── README.md          # Task documentation
```
