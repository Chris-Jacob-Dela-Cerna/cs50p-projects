# Document: This python is my 1st application of CS50P Week 6.

questions = {
    "Age": "What's your age?",
    "Gender": "Are you a male or female?",
    "Location": "Where are you currently located?",
    "Education Level": "What is the highest education you've attained?",
    "Employment Status": "Are you currently employed or no?",
}

for question in questions:
    demo = input(f"System:   {question}").strip().title()