"""
CareerBot - AI Career Assistant
--------------------------------
A simple RULE-BASED chatbot (no AI models, no APIs).

How it decides what to say:
1. The user's message is normalized (lowercased, extra spaces removed).
2. We check the normalized message against a list of (keywords, response) rules.
3. Rules are checked in order from most specific (multi-word phrases like
   "machine learning") to more general (single words like "ai"). This stops
   a generic rule from "stealing" a match that a more specific rule should
   have answered.
4. The FIRST rule whose keyword is found inside the user's message wins,
   and its response is returned.
5. If no rule matches, we return a fallback response instead of guessing.

This project intentionally does NOT use OpenAI/Claude/Gemini APIs,
machine learning models, web scraping, or a database — just plain Python.
"""

import re

# ---------------------------------------------------------------------------
# RULES TABLE
# Each rule is a tuple: (list_of_keywords, response_text)
# Order matters: more specific phrases are placed BEFORE generic ones.
# ---------------------------------------------------------------------------
RULES = [
    # Greetings
    (
        ["hi", "hello", "hey", "good morning", "good afternoon", "good evening"],
        "Hello! 👋 I'm CareerBot, your career assistant. How can I help you today?"
    ),

    # About CareerBot
    (
        ["who are you", "what are you", "what can you do", "tell me about yourself", "help"],
        "I'm CareerBot 🤖 — a rule-based career assistant built in Python.\n"
        "I match keywords in your questions to predefined answers about AI, "
        "programming, and career topics. I don't use any external AI models."
    ),

    # AI Engineer Career (checked before generic "ai" rule)
    (
        ["ai engineer", "ai developer", "become ai engineer", "ai engineering career", "ai career path"],
        "Here's a simple AI Engineer roadmap:\n"
        "  Python -> Mathematics Basics -> Data Handling -> Machine Learning\n"
        "  -> Deep Learning -> AI Projects -> GitHub Portfolio -> Internship/Job\n"
        "Take it one step at a time and build small projects along the way!"
    ),

    # AI Skills (checked before generic "ai" rule)
    (
        ["ai skills", "skills for ai", "ai engineer skills", "skills needed for ai",
         "skills do i need", "what skills"],
        "Key skills for an AI career include:\n"
        "  - Python\n  - Mathematics (stats, linear algebra basics)\n"
        "  - Machine Learning fundamentals\n  - Data Handling\n"
        "  - Problem Solving\n  - Hands-on Projects\n  - Git/GitHub"
    ),

    # Machine Learning (checked before generic "ai")
    (
        ["machine learning", "ml", "what is ml"],
        "Machine Learning is a branch of Artificial Intelligence that allows "
        "computers to learn patterns from data and make predictions or decisions "
        "without being explicitly programmed for every situation."
    ),

    # Artificial Intelligence (generic - checked after ML/AI-engineer/AI-skills)
    (
        ["artificial intelligence", "what is ai", "learn ai", "ai"],
        "Artificial Intelligence (AI) is the field of computer science focused on "
        "building systems that can perform tasks that normally require human "
        "intelligence, such as understanding language, recognizing patterns, or "
        "making decisions."
    ),

    # Python
    (
        ["python developer", "why learn python", "learn python", "python programming", "python"],
        "Python is a beginner-friendly, versatile programming language widely used "
        "in AI, Machine Learning, web development, data science, and automation. "
        "Its simple syntax makes it a great first language."
    ),

    # Programming (generic - checked after Python so "python programming" hits Python first)
    (
        ["programming language", "learn coding", "coding skills", "programming", "coding"],
        "Programming is the process of writing instructions for computers to "
        "follow. Strong programming skills are valuable for almost every "
        "technology career, from software development to AI engineering."
    ),

    # Web Development
    (
        ["web development", "web developer", "frontend", "backend", "website development"],
        "Web Development is split into two main areas:\n"
        "  - Frontend: what users see and interact with (HTML, CSS, JavaScript)\n"
        "  - Backend: the server, database, and logic behind the scenes\n"
        "Full-stack developers work on both sides."
    ),

    # Data Science
    (
        ["data science", "data scientist", "learn data science"],
        "Data Science involves analyzing and interpreting data to find useful "
        "insights. Core skills include Python, data analysis, statistics, and "
        "data visualization."
    ),

    # Career Guidance (generic - checked before generic single words don't conflict here)
    (
        ["career path", "career choice", "which career", "choose a career",
         "technology career", "career"],
        "Choosing a career path is a personal decision. Think about your "
        "interests, current skills, education, and long-term goals. Try "
        "exploring a few areas (like AI, web development, or data science) "
        "through small projects before committing to one path."
    ),

    # Resume / CV
    (
        ["resume for developer", "technical resume", "resume tips", "cv tips", "resume", "cv"],
        "Resume tips for tech roles:\n"
        "  - Contact information\n  - Career objective/summary\n  - Education\n"
        "  - Technical skills\n  - Projects\n  - Internship/experience\n"
        "  - Certifications\n"
        "Keep it concise, clear, and tailored to the role you're applying for."
    ),

    # Interview Preparation
    (
        ["interview preparation", "technical interview", "interview tips",
         "job interview", "interview"],
        "Interview preparation basics:\n"
        "  - Review core concepts for the role (e.g. Python, ML basics)\n"
        "  - Practice explaining your projects clearly\n"
        "  - Solve practice coding problems\n"
        "  - Prepare questions to ask the interviewer\n"
        "  - Get a good night's sleep before the interview!"
    ),

    # Internship
    (
        ["how to get internship", "internship tips", "internships", "internship"],
        "Tips for landing an internship:\n"
        "  - Build small, genuine projects\n  - Maintain an active GitHub profile\n"
        "  - Prepare a clear, honest resume\n  - Practice your technical skills\n"
        "  - Apply consistently and don't get discouraged by rejections"
    ),

    # GitHub / Portfolio
    (
        ["github portfolio", "developer portfolio", "github", "portfolio", "projects"],
        "GitHub lets you showcase your code and projects publicly. A strong "
        "portfolio of real projects (even small ones) demonstrates your skills "
        "to employers far better than a resume alone."
    ),
]

# ---------------------------------------------------------------------------
# Exit keywords - checked separately from RULES since they end the program
# ---------------------------------------------------------------------------
EXIT_KEYWORDS = ["bye", "goodbye", "exit", "quit", "see you", "see you later"]

FALLBACK_RESPONSE = (
    "I'm sorry, I don't have information about that yet. I can help with AI, "
    "Machine Learning, Python, programming, web development, careers, resumes, "
    "interviews, internships, and GitHub."
)


def show_welcome():
    """Prints the chatbot introduction banner."""
    print("=" * 40)
    print("🤖 CAREERBOT")
    print("AI Career Assistant")
    print("=" * 20)
    print()
    print("CareerBot: Hello! I'm CareerBot.")
    print("I can help you with:")
    print("  • AI")
    print("  • Machine Learning")
    print("  • Python")
    print("  • Programming")
    print("  • Careers")
    print("  • Resume")
    print("  • Interviews")
    print("  • Internships")
    print("  • GitHub")
    print()
    print("Type 'bye' or 'exit' to end the conversation.")
    print()


def normalize_input(user_input):
    """Lowercases and strips extra whitespace so matching is consistent
    no matter how the user capitalizes or spaces their message."""
    return user_input.lower().strip()


def contains_keyword(cleaned_input, keyword):
    """Checks whether `keyword` appears in `cleaned_input` as a whole
    word/phrase (not as part of a bigger word). We use a word-boundary
    regex so that short keywords like 'hi' or 'ai' don't accidentally
    match inside unrelated words like 'machine' or 'internship'."""
    pattern = r"\b" + re.escape(keyword) + r"\b"
    return re.search(pattern, cleaned_input) is not None


def is_exit_command(cleaned_input):
    """Returns True if the cleaned input matches an exit keyword."""
    return any(contains_keyword(cleaned_input, keyword) for keyword in EXIT_KEYWORDS)


def get_response(cleaned_input):
    """Checks the cleaned input against every rule in RULES, in order.
    Returns the response for the first matching keyword found.
    If nothing matches, returns the fallback response."""
    for keywords, response in RULES:
        for keyword in keywords:
            if contains_keyword(cleaned_input, keyword):
                return response
    return FALLBACK_RESPONSE


def chatbot():
    """Main conversation loop: get input, normalize, respond, repeat
    until the user types an exit command."""
    show_welcome()

    while True:
        user_input = input("You: ")
        cleaned = normalize_input(user_input)

        if cleaned == "":
            continue  # ignore empty input, ask again

        if is_exit_command(cleaned):
            print()
            print("CareerBot: Goodbye! 👋 Good luck with your career journey!")
            print()
            print("=" * 40)
            print("CHAT ENDED")
            print("=" * 10)
            break

        response = get_response(cleaned)
        print()
        print(f"CareerBot: {response}")
        print()


if __name__ == "__main__":
    chatbot()
