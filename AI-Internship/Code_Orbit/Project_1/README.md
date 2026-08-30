# CareerBot — AI Career Assistant

## Overview

CareerBot is a terminal-based chatbot built in Python that answers common questions about AI, programming, and career development. It was created as a beginner-friendly project to demonstrate how a **rule-based chatbot** works — no external AI, no machine learning, just clean logic.

## Objective

This project demonstrates a rule-based chatbot that uses predefined keywords and canned responses to answer user questions. It shows how `if/elif`, keyword matching, dictionaries, and functions can be combined to build an interactive command-line assistant, without relying on any generative AI model or API.

## Features

- Handles common greetings (hi, hello, hey, good morning, etc.)
- Answers questions across 15 predefined topic categories
- Friendly fallback response for unrecognized input
- Case-insensitive and whitespace-tolerant input handling
- Polite exit/goodbye system (bye, exit, quit, etc.)
- Clean, professional terminal interface
- Continuous conversation loop until the user exits

### Topics CareerBot Can Discuss

- Greeting recognition (hi, hello, hey, good morning, etc.)
- "About CareerBot" responses
- Artificial Intelligence explanations
- Machine Learning explanations
- Python guidance
- Programming/coding guidance
- Web Development (frontend vs backend) explanation
- Data Science overview
- AI Engineer career roadmap
- General career guidance
- AI skills breakdown
- Resume/CV tips
- Interview preparation tips
- Internship advice
- GitHub/portfolio guidance
- Polite exit handling (bye, goodbye, exit, quit, see you)
- Friendly fallback response for unrecognized input
- Input normalization (case-insensitive, whitespace-tolerant)

## Technologies Used

- Python 3
- Conditional statements (`if` / `elif` / `else`)
- Keyword matching (`re` module, word-boundary regex)
- Functions
- Loops (`while True` conversation loop)
- String processing

## How It Works

CareerBot works by comparing normalized user input against lists of predefined keywords, and returning the response tied to the first matching rule.

- **User Input** — the raw text typed by the user.
- **Input Normalization** — the input is lowercased and stripped of extra whitespace so that "Hi", "HI", and " hi " are all treated the same way.
- **Keyword Detection** — the normalized input is checked against keyword lists (e.g., "machine learning", "ai", "resume") using simple substring matching.
- **Rule Matching** — rules are checked in order, with more specific multi-word phrases checked before shorter, more generic ones to avoid the wrong topic firing.
- **Predefined Response** — if a rule matches, its associated response is printed. If nothing matches, a fallback message is shown instead.

## Project Structure

```
CodeOrbit_CareerBot/Project_1
│
├── careerbot.py
├── README.md
└── screenshots/
    └── chatbot_demo.png
```

### Diagram

```
User Input
    ↓
Normalize Input (lowercase, strip spaces)
    ↓
Check Keywords Against Rules
    ↓
Matching Rule?
├── YES → Return Predefined Response
└── NO  → Return Fallback Response
    ↓
Check for Exit Command
├── YES → Goodbye Message → END
└── NO  → Continue Conversation
```

## How to Run

```bash
python careerbot.py
```

(On some systems you may need `python3 careerbot.py` instead.)

## Example Conversation

```
========================================
🤖 CAREERBOT
AI Career Assistant
====================

CareerBot: Hello! I'm CareerBot.
I can help you with:
  • AI
  • Machine Learning
  • Python
  • Programming
  • Careers
  • Resume
  • Interviews
  • Internships
  • GitHub

Type 'bye' or 'exit' to end the conversation.

You: What is AI?

CareerBot: Artificial Intelligence (AI) is the field of computer science focused on building systems that can perform tasks that normally require human intelligence, such as understanding language, recognizing patterns, or making decisions.

You: How can I get an internship?

CareerBot: Tips for landing an internship:
  - Build small, genuine projects
  - Maintain an active GitHub profile
  - Prepare a clear, honest resume
  - Practice your technical skills
  - Apply consistently and don't get discouraged by rejections

You: bye

CareerBot: Goodbye! 👋 Good luck with your career journey!

========================================
CHAT ENDED
==========
```

## Testing

The project was manually tested against the following inputs to confirm each category returns the correct predefined response, and that unrecognized input correctly triggers the fallback:

1. Hello
2. Hi
3. Who are you?
4. What is AI?
5. What is Machine Learning?
6. Why should I learn Python?
7. What is programming?
8. What is web development?
9. What is Data Science?
10. How can I become an AI engineer?
11. What skills do I need for AI?
12. How can I improve my resume?
13. How should I prepare for an interview?
14. How can I get an internship?
15. What is GitHub?
16. An unknown/unrelated question
17. Bye

## Limitations

- CareerBot is **rule-based only** — it does not use machine learning or
  generative AI in any form.
- It cannot understand every possible phrasing of a question.
- It only responds to predefined topics and keywords listed above.
- It has no memory of previous messages within a conversation.

## Future Improvements

These are potential ideas for later versions — not implemented here:

- A graphical user interface (GUI)
- A database of responses instead of hardcoded rules
- Basic NLP for more flexible language understanding
- Optional AI API integration for open-ended questions
- A larger, more detailed knowledge base

## Internship Context

This project was developed as part of the **CodeOrbit Tech Artificial Intelligence Internship** (1-Month Program) as a demonstration of rule-based chatbot logic in Python. It does not use machine learning or generative AI — all responses come from predefined rules.
