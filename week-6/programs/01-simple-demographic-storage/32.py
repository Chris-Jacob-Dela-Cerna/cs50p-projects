# Document: This python is my 1st application of CS50P Week 6.

questions = {
    "Age": "What's your age?",
    "Gender": "Are you a male or female?",
    "Location": "Where are you currently located?",
    "Education Level": "What is the highest education you've attained?",
    "Employment Status": "Are you currently employed or no?",
}

user = {}
for demographic, question in questions.items():
    user_demo = input(f"System:   {question}").strip().title()
    user.update({demographic: user_demo})

with open("recent_demo.txt", "w") as stored:
    stored.write()