import sys
import time
import random
from datetime import datetime

BOT_NAME = "Nova"

def typing_print(text, delay=0.03):
    """Prints text with a typing animation effect."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print() # newline at the end

def normalize_input(user_input):
    """
    Normalizes the input by stripping leading/trailing whitespace and converting to lowercase.
    """
    return user_input.strip().lower()

def get_response(user_input):
    """
    Determines the bot's response based on rule-based pattern matching.
    """
    text = normalize_input(user_input)
    
    if not text:
        return "Please say something! 😅"

    # 1. Greeting
    if any(greeting in text for greeting in ['hello', 'hi', 'hey', 'good morning', 'good afternoon', 'good evening']):
        return "Hi! 👋 Nice to meet you. How can I help? 😊"
        
    # 2. How the chatbot is doing
    elif any(phrase in text for phrase in ['how are you', 'how are you doing', 'how is it going']):
        return "I'm doing great! ✨ Thanks for asking. How can I assist you today?"
        
    # 3. Identity
    elif any(phrase in text for phrase in ['who are you', 'what are you', 'what is your name']):
        return f"I am {BOT_NAME} 🤖, a simple rule-based chatbot created for the CODSOFT AI Internship Task 1."
        
    # 3.5. Date and Time
    elif any(phrase in text for phrase in ['current date', 'what day is it', 'what is the date', "today's date", 'what time is it', 'current time']):
        now = datetime.now()
        return f"Today is {now.strftime('%B %d, %Y')} 📅 and the current time is {now.strftime('%I:%M %p')} ⏰."
        
    # 4. Capabilities
    elif any(phrase in text for phrase in ['what can you do', 'help', 'what do you know']):
        return ("Here is a list of things I can do 🛠️:\n"
                "     - Answer basic questions about AI and machine learning 🧠.\n"
                "     - Tell you the current date and time ⏳.\n"
                "     - Tell you a joke 😂.\n"
                "     - Explain this CODSOFT internship project 💻.\n"
                "     - Have simple greetings and conversations 💬.\n"
                "     - Type 'exit', 'quit', or 'bye' to end the chat 👋.")
                
    # 5. AI-related basic questions (Expanded to answer related questions)
    elif any(keyword in text for keyword in ['what is ai', 'artificial intelligence', 'define ai']):
        return "Artificial Intelligence (AI) 🧠 is the simulation of human intelligence by computer systems. It involves learning, reasoning, and self-correction!"
    elif any(keyword in text for keyword in ['what is machine learning', 'machine learning', 'ml']):
        return "Machine Learning (ML) 📈 is a branch of AI where computers learn patterns from data without being explicitly programmed."
    elif any(keyword in text for keyword in ['deep learning', 'dl']):
        return "Deep Learning 🕸️ is a subset of ML based on artificial neural networks. It's the tech behind things like ChatGPT and self-driving cars!"
    elif any(keyword in text for keyword in ['nlp', 'natural language processing']):
        return "Natural Language Processing (NLP) 🗣️ is a field of AI that gives machines the ability to read, understand, and derive meaning from human languages."
    elif any(keyword in text for keyword in ['data science']):
        return "Data Science 📊 combines domain expertise, programming skills, and knowledge of math and statistics to extract meaningful insights from data."
    elif any(keyword in text for keyword in ['neural network', 'neural networks']):
        return "Neural Networks 🧠 are computing systems inspired by the biological neural networks that constitute animal brains."
        
    # 6. Internship/project-related questions
    elif any(phrase in text for phrase in ['what is this project', 'what is this chatbot', 'codsoft']):
        return "This is Task 1 of the CODSOFT AI Internship 🚀, focusing on building a rule-based chatbot."
    elif any(phrase in text for phrase in ['why is it rule based', 'rule-based', 'rule based']):
        return "It is rule-based 📜 to demonstrate basic NLP concepts and conversation flow using pattern matching instead of machine learning models."
        
    # 6.5. Joke
    elif any(phrase in text for phrase in ['joke', 'make me laugh', 'funny']):
        jokes = [
            "Why do programmers prefer dark mode? Because light attracts bugs! 🐛",
            "How many programmers does it take to change a light bulb? None, that's a hardware problem. 💡",
            "Why did the programmer quit his job? Because he didn't get arrays. 👨‍💻",
            "There are 10 types of people in the world: those who understand binary, and those who don't. 🔢"
        ]
        return random.choice(jokes)
        
    # 7. Thanks
    elif any(phrase in text for phrase in ['thanks', 'thank you', 'thank you so much']):
        return "You're welcome! 😇 Glad I could help."
        
    # 8. Goodbye / Exit (handled mostly in main loop, but here as a fallback)
    elif any(phrase in text for phrase in ['bye', 'goodbye', 'exit', 'quit']):
        return "Goodbye! 👋 Have a great day! 🌟"
        
    # Fallback for unknown queries
    else:
        return ("I'm still learning! 😅 I don't have a rule for that question yet.\n"
                "     Try asking me about AI, Machine Learning, Deep Learning, my capabilities, or type 'help' ℹ️.")

def main():
    print("==================================================")
    print(f"        CODSOFT AI - {BOT_NAME.upper()} CHATBOT")
    print("==================================================")
    print()
    typing_print(f"{BOT_NAME}: Hello! 👋 I'm {BOT_NAME} 🤖, a simple rule-based chatbot.")
    typing_print(f"{BOT_NAME}: Type 'help' to see what I can do. ✨")
    typing_print(f"{BOT_NAME}: Type 'exit' or 'bye' to end the conversation. ❌")
    print()

    while True:
        try:
            user_input = input("You: ")
            
            normalized_input = normalize_input(user_input)
            
            # Check for exit commands explicitly to break the loop
            if normalized_input in ['exit', 'quit', 'bye', 'goodbye']:
                typing_print(f"{BOT_NAME}: Goodbye! 👋 Have a great day! 🌟")
                print("==================================================")
                break
                
            response = get_response(user_input)
            sys.stdout.write(f"{BOT_NAME}: ")
            sys.stdout.flush()
            typing_print(response)
            print()
            
        except (KeyboardInterrupt, EOFError):
            # Gracefully handle Ctrl+C or Ctrl+D
            print()
            typing_print(f"{BOT_NAME}: Goodbye! 👋 Have a great day! 🌟")
            print("==================================================")
            break

if __name__ == "__main__":
    main()
