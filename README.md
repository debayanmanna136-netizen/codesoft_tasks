# 🚀 CODSOFT AI & Machine Learning Internship

<div align="center">

[![GitHub Repo Size](https://img.shields.io/github/repo-size/debayanmanna136-netizen/codesoft_tasks?style=for-the-badge&color=blue)](https://github.com/debayanmanna136-netizen/codesoft_tasks)
[![Python Version](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)](https://pytorch.org/)
[![HuggingFace Transformers](https://img.shields.io/badge/Hugging%20Face-Transformers-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)](https://huggingface.co/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)

**Repository containing all three assigned tasks for the CODSOFT Artificial Intelligence & Machine Learning Internship.**  
Developed by **Debayan Manna**

[Explore Tasks](#-internship-tasks-overview) • [Installation Guide](#-quick-start--installation) • [Repository Structure](#-repository-structure)

</div>

---

## 📋 Internship Tasks Overview

Each task is self-contained in its own dedicated, clearly distinguished directory with code, documentation, and interface assets:

| # | Task Directory | Domain | Model / Algorithm | Interfaces | Status |
|:---:|:---|:---|:---|:---:|:---:|
| **01** | [**`Task-1_Chatbot`**](./Task-1_Chatbot) | Natural Language Processing | Rule-based Intent Matching & Heuristics | 🖥️ CLI | ✅ Completed |
| **02** | [**`Task-2_TicTacToe_AI`**](./Task-2_TicTacToe_AI) | Game Theory / Adversarial Search | Minimax Algorithm + Alpha-Beta Pruning | 🖥️ CLI & 🌐 Web App | ✅ Completed |
| **03** | [**`Task-3_Image_Captioning`**](./Task-3_Image_Captioning) | Computer Vision & NLP | BLIP Vision-Language Foundation Model | 🖥️ CLI & 🌐 Web Server | ✅ Completed |

---

## 🤖 Task 1: Rule-Based Chatbot (`Nova`)

> **Directory**: [`Task-1_Chatbot/`](./Task-1_Chatbot)  
> **Key Technologies**: Python Standard Library, String Normalization, Intent Classification

An interactive conversational chatbot (`Nova`) demonstrating foundational Natural Language Processing (NLP) techniques without external large language model dependencies.

### Key Highlights:
- **Typing Animation Simulation**: Delivers a dynamic, live terminal conversational experience.
- **Intent Pattern Matching**: Accurately recognizes greetings, identity queries, capability help, time/date inquiries, and educational FAQs on AI/ML.
- **Robust Fallback Engine**: Gracefully handles unknown queries with conversational prompts.

```bash
# Run Task 1
cd Task-1_Chatbot
python chatbot.py
```

---

## 🎮 Task 2: Unbeatable Tic-Tac-Toe AI

> **Directory**: [`Task-2_TicTacToe_AI/`](./Task-2_TicTacToe_AI)  
> **Key Technologies**: Minimax Algorithm, Alpha-Beta Pruning, HTML5/CSS3/JS, ANSI Terminal

An adversarial search AI agent designed to play the classic game of Tic-Tac-Toe against a human player. Utilizing **Minimax with Alpha-Beta Pruning**, the agent is mathematically proven to be **unbeatable** on Hard difficulty.

### Key Highlights:
- **Dual Interfaces**:
  - 🌐 **Modern Web Game** (`tictactoe.html`): Dark glassmorphism aesthetic with glowing neon lines, animated winning combos, live scoreboard, and 2-player mode.
  - 🐍 **Colorized Terminal CLI** (`tictactoe.py`): ANSI-colored board rendering with round history tracking.
- **Difficulty Selection**:
  - `Easy`: Random cell selection.
  - `Medium`: Balanced 50/50 heuristic-optimal strategy.
  - `Hard`: Full Minimax with Alpha-Beta pruning ($O(b^{d/2})$ complexity).

```bash
# Option A: Open the interactive Web UI
start Task-2_TicTacToe_AI/tictactoe.html

# Option B: Run the Python CLI
cd Task-2_TicTacToe_AI
python tictactoe.py
```

---

## 🖼️ Task 3: Deep Learning Image Captioning

> **Directory**: [`Task-3_Image_Captioning/`](./Task-3_Image_Captioning)  
> **Key Technologies**: Salesforce BLIP (`blip-image-captioning-base`), PyTorch, Hugging Face Transformers, Pillow

An end-to-end Deep Learning system that bridges Computer Vision and Natural Language Generation. By utilizing **transfer learning** with Salesforce's pre-trained **BLIP** vision-language model, it extracts rich visual representations and decodes them into fluent English captions.

### Key Highlights:
- **Vision-Language Foundation**: Uses a Vision Transformer (ViT) encoder coupled with an autoregressive text decoder.
- **Dual Usage Modes**:
  - 🖥️ **CLI Mode** (`image_captioning.py`): Batch and interactive single-image captioning with persistent logging to `outputs/captions.txt`.
  - 🌐 **Local Web Application** (`server.py`): Browser-based interface enabling users to upload any picture and inspect real-time generated captions.
- **Comprehensive Reports**: Includes detailed project reports in [`docs/`](./Task-3_Image_Captioning/docs).

```bash
# Install dependencies
cd Task-3_Image_Captioning
pip install -r requirements.txt

# Run CLI inference
python image_captioning.py

# Or launch local web server
python server.py
# Open http://localhost:8000 in your browser
```

---

## 📂 Repository Structure

```text
codesoft_tasks/
├── .gitignore                          # Clean git ignore configuration
├── LICENSE                             # MIT Open-Source License
├── README.md                           # Master repository documentation (this file)
│
├── Task-1_Chatbot/                     # ── TASK 1: RULE-BASED CHATBOT ──
│   ├── chatbot.py                      # Main chatbot implementation
│   ├── requirements.txt                # Dependency list
│   └── README.md                       # Task 1 detailed documentation
│
├── Task-2_TicTacToe_AI/                # ── TASK 2: TIC-TAC-TOE AI AGENT ──
│   ├── tictactoe.py                    # Terminal CLI with ANSI color board
│   ├── tictactoe.html                  # Interactive modern Web Application
│   ├── requirements.txt                # Dependency list
│   └── README.md                       # Task 2 detailed documentation
│
└── Task-3_Image_Captioning/            # ── TASK 3: IMAGE CAPTIONING ──
    ├── image_captioning.py             # CLI inference script
    ├── server.py                       # Local Web UI server for image uploads
    ├── sample_images/                  # Curated benchmark test images
    │   ├── image1.jpg                  # Person in park
    │   ├── image2.jpg                  # Dog in grass
    │   └── image3.jpg                  # Landscape
    ├── outputs/                        # Saved inference output logs
    │   ├── captions.txt                # Formatted caption log file
    │   └── image_captioning_result.png # Sample generation screenshot
    ├── docs/                           # Formal reports & documentation
    │   ├── Project_Report.md           # Technical task report
    │   ├── Project_Report.pdf          # Formatted PDF task report
    │   ├── Final_Task_Report.md        # Comprehensive internship report
    │   └── Final_Task_Report.pdf       # Formatted PDF internship report
    ├── requirements.txt                # PyTorch & Transformers dependencies
    └── README.md                       # Task 3 detailed documentation
```

---

## ⚡ Quick Start & Installation

### 1. Clone the Repository
```bash
git clone https://github.com/debayanmanna136-netizen/codesoft_tasks.git
cd codesoft_tasks
```

### 2. Set Up a Virtual Environment (Recommended)
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On Linux/macOS
source venv/bin/activate
```

### 3. Install Dependencies
Task 1 and Task 2 require only the standard library. For Task 3:
```bash
pip install -r Task-3_Image_Captioning/requirements.txt
```

---

## 👨‍💻 Author

- **Name**: Debayan Manna
- **Internship**: CODSOFT Artificial Intelligence & Machine Learning Internship
- **GitHub**: [@debayanmanna136-netizen](https://github.com/debayanmanna136-netizen)
