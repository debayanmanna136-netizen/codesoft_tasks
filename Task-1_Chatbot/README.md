# Task 1 · Rule-Based Chatbot (Nova)

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![NLP](https://img.shields.io/badge/NLP-Rule--Based-blueviolet?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

A smart, interactive, rule-based conversational agent built in Python for the **CODSOFT AI Internship (Task 1)**.

---

## 📌 Project Overview

This project demonstrates the core concepts of conversational Natural Language Processing (NLP) without relying on heavyweight external APIs or large language models. The chatbot uses input normalization, token pattern matching, intent classification, and structured fallback mechanisms to converse naturally with human users.

---

## 🚀 Key Features

- **Dynamic Typing Animation**: Simulates a live human/AI typing effect in the terminal.
- **Intent Recognition Pipeline**:
  - 👋 **Greetings & Salutations**: Handles multiple greeting patterns (*hello, hi, hey, good morning/evening*).
  - 🤖 **Identity & Purpose**: Explains its name, origin, and task description.
  - 📅 **Live Date & Time**: Real-time clock and calendar reporting.
  - 🧠 **AI / ML Educational FAQs**: Clear definitions for Artificial Intelligence, Machine Learning, Deep Learning, and NLP.
  - 😂 **Entertainment**: Built-in jokes and fun interactions.
  - 🛠️ **Capability Help**: Interactive menu of supported commands.
  - 🚪 **Safe Exit**: Graceful shutdown on *exit, quit, bye*.
- **Robust Fallback Engine**: Friendly responses when the query does not match known patterns.

---

## 🏗️ Architecture & Conversation Pipeline

```text
       User Terminal Input
                │
                ▼
     Input Normalization
   (Lowercase, Trim spaces)
                │
                ▼
     Pattern & Intent Matcher
   (Keywords, Regex, Synonyms)
   ┌────────────┬────────────┐
   ▼            ▼            ▼
[Greetings]   [FAQs]     [Fallback]
   │            │            │
   └────────────┼────────────┘
                ▼
      Typing Effect Output
```

---

## 💻 How to Run

### 1. Requirements
Only Python's standard library is required (`sys`, `time`, `random`, `datetime`).

### 2. Execution
```bash
# Navigate to Task 1 directory
cd Task-1_Chatbot

# Run the chatbot
python chatbot.py
```

---

## 📸 Sample Interaction

```text
Nova: Hello! 👋 I am Nova, your virtual AI assistant.
You: what can you do
Nova: Here is a list of things I can do 🛠️:
     - Answer basic questions about AI and machine learning 🧠.
     - Tell you the current date and time ⏳.
     - Tell you a joke 😂.
     - Explain this CODSOFT internship project 💻.
     - Have simple greetings and conversations 💬.
     - Type 'exit', 'quit', or 'bye' to end the chat 👋.

You: what is ai
Nova: Artificial Intelligence (AI) 🧠 is the simulation of human intelligence by computer systems. It involves learning, reasoning, and self-correction!
```
