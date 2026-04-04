# Document: This python is my 2nd application of CS50P Week 1.

# An easy access question list that can be used by the program using global variables. It is placed outside defined functions so that the any part of the program can run them
q1 = "1. It is an effective instrument for promoting and spreading relevant advocacies on social change. \na. Social media \nb. ICT \nc. Discovery \nd. Diffusion \nAnswer: "
q2 = "2. It is the adjustment in human interactions, which changes the established cultural and social constructs, beliefs, and institutions. \na. Social justice \nb. Cultural shift \nc. Social change \nd. Advocacy \nAnswer: "
q3 = "3. The stage wherein new forms of technology are developed. \na. Diffusion \nb. Discovery \nc. Innovation \nd. Invention \nAnswer: "
q4 = "4. Refers to new ways of understanding and perceiving reality. \na. Discovery \nb. Diffusion \nc. Invention \nd. Adaptation \nAnswer: "
q5 = "5. Refers to the spread of technology from the point of discovery to other areas. \na. Discovery \nb. Diffusion \nc. Invention \nd. Distribution \nAnswer: "
q6 = "6. Social media is the best tool for spreading advocacies and causes than other forms of technology. \na. The Role of ICT \nb. Social Change \nc. The Social Power of Social Media \nd. Ogburn’s Theory \nAnswer: "
q7 = "7. Social media can create online spaces where people come together and find support, such as creating a space for sharing ideas online that creates unity for a cause. \na. Sharing Pictures and Videos \nb. Platforming Lived Experience \nc. Coordinating Community Responses \nd. Online Campaigning \nAnswer: "
q8 = "8. Social justice causes aim to achieve equity for minorities and underrepresented individuals and groups, as their stories and struggles are not often known and publicized. \na. Sharing Pictures and Videos \nb. Platforming Lived Experience \nc. Coordinating Community Responses \nd. Social Broadcasting \nAnswer: "
q9 = "9. Social media is not just a tool for organizing large-scale protests but also for documenting them. \na. Sharing Pictures and Videos \nb. Platforming Lived Experience \nc. Coordinating Community Responses \nd. Digital Archiving \nAnswer: "
q10 = "10. Refers to simple measures to support a social movement online, such as signing petitions and copying and reposting statuses and images. \na. Cancel culture \nb. Online activism \nc. Slacktivism \nd. Digital protest \nAnswer: "

# A global tuple list for the correct answers. A tuple list is used to compile all correct answers instead of listing correct1, ...
correct = ("b","c","d","a","b","c","c","b","a","c")

def greet():
# Each time I use print() only, this is used to space out text when the python is run
    print()
# Greets user and introduces the system
    print("Greetings, this is my very first program using a quiz system :)")

def start():
    print()
# Prompts the user if they want to start, exits if not
    if_start = input("Ready to start the quiz? (y or n): ").strip().lower()
# Returns the response to main()/start()/ to see if the user chooses to proceed with "y"
    return if_start == "y"

# This function makes it easier to run each q(#) using a reusable prompt
# Grabs each q(#) from quiz() 1 by 1 in a placeholder called "question".
def ques(question):
# Releases the variable from "question" and inserts it in a prompt. Prompts the user for an answer then 
    answer = input(question).strip().lower()
# Returns and stores the answers in quiz()'s variables like "a1"
    return answer

def quiz():
    print()
# Introduces the questionnaire to the user
    print("This is a multiple choice questionnaire. \nAnswer a, b, c, d only.")

    print()
# Takes each q(#) 1 by 1 and processes them through ques(). 
    a1 = ques(q1)
    print()
    a2 = ques(q2)
    print()
    a3 = ques(q3)
    print()
    a4 = ques(q4)
    print()
    a5 = ques(q5)
    print()
    a6 = ques(q6)
    print()
    a7 = ques(q7)
    print()
    a8 = ques(q8)
    print()
    a9 = ques(q9)
    print()
    a10 = ques(q10)
# A tuple list for the answers. This is so that check_quiz can define each a(#) through "answer"
    answer = (a1, a2, a3, a4, a5, a6, a7, a8, a9, a10)
# Returns the answer to check_quiz() and main()/start()/quiz()/check_quiz()/
    return answer

# This function checks all answers and sums up a final score
# Grabs the tuple list of "answer" and "correct".
def check_quiz(answer, correct):
# Decompiles the tuple list of answer for check_quiz()
    a1, a2, a3, a4, a5, a6, a7, a8, a9, a10 = answer
# Decompiles the tuple list of correct for check_quiz()
    correct1, correct2, correct3, correct4, correct5, correct6, correct7, correct8, correct9, correct10 = correct
# Sets a starting score of 0
    score = 0
# "if" system checks for correct answers, then each correct answer is 1 point added to score using "+= 1"
    if a1 == correct1:
        score += 1
    if a2 == correct2:
        score += 1
    if a3 == correct3:
        score += 1
    if a4 == correct4:
        score += 1
    if a5 == correct5:
        score += 1
    if a6 == correct6:
        score += 1
    if a7 == correct7:
        score += 1
    if a8 == correct8:
        score += 1
    if a9 == correct9:
        score += 1
    if a10 == correct10:
        score += 1
# Returns the final score to results() and main()/start()/quiz()/check_quiz()/results()
    return score

# Grabs the score from check_quiz()
def results(score):
    print()
# Congratulates the user and announces their final score
    print(f"Congratulations! You've got a total score of {score}/10.")

def retake():
    print()
# Prompts user if they want to retake the quiz
    if_retake = input("Retake? (y or n) ").strip().lower()
# Returns the response to main()/start()/quiz()/check_quiz()/results()/retake() to see if the user chooses to proceed with "y"
    return if_retake == "y"

def exiting():
    print()
# Sends exiting message
    print("Exiting...")
    print()
# Exits the program
    raise SystemExit()

# Runs entire program
def main():
# Checks if user chose "y" to continue or "n" to exit
    if start():
# Runs quiz() then stores answers in a variable
        answer = quiz()
# Runs check_quiz() while using variables "answer" and "correct", then stores the score in a variable
        score = check_quiz(answer, correct)
# Runs results()
        results(score)
# Checks if user chose "y" to retake or "n" to exit. Retake starts main() again
        if retake():
            main()
        else:
            exiting()
    else:
        exiting()

# Greets the user upon starting the program
greet()

main()