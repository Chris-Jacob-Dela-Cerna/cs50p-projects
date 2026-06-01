# Document: This python is my 1st application of CS50P Week 6.

questions = {
    "Age": "What's your age?",
    "Gender": "Are you a male or female?",
    "Location": "Where are you currently located?",
    "Education Level": "What is the highest education you've attained?",
    "Employment Status": "Are you currently employed or no?",
}


user = []
for demo, question in questions.items():
    result = input(f"System:   {question} ").strip().title()
    user.append({"demographic": demo, "user_demo": result})


def format_data():
    return f"""{user[0]['demographic']}: {user[0]["user_demo"]}
{user[1]['demographic']}: {user[1]["user_demo"]}
{user[2]['demographic']}: {user[2]["user_demo"]}
{user[3]['demographic']}: {user[3]["user_demo"]}
{user[4]['demographic']}: {user[4]["user_demo"]}"""


with open("recent_demo.txt", "w") as stored:
    stored.write(format_data())