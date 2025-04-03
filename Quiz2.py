# NUIST Quiz Game in Python
def quiz():
    print("Welcome to the Animal Quiz!")
    print("Answer the following questions:")

# Questions and Answers
    questions = [
        "1. Which of the following is NOT a python data type?
a) int
b) float
c) rational
d) string
e) bool”,
 
        "2.Which of the following is NOT a built - in operation in Python?
a) +
b) %
c) abs()
d) sqrt()",

        "3. In a mixed - type expression involving ints and floats, Python will convert:
a) floats to ints
b) ints to strings
c) floats and ints to strings
d) ints to floats "，

         "4. The best structure for implementing a multi - way decision in Python is:
a) if
b) if - else
c) if - elif - else
d) try",

         "5. What statement can be executed in the body of a loop to cause it to terminate?
a) if
b) exit
c) continue
d) break"
    ]
    answers = [
        "rational",
        "sqrt()",
        "ints to floats",
        "if - elif - else",
        "exit"
    ]
    score = 0

# Ask questions
    for i in range(len(questions)):
        user_answer = input(questions[i]).strip().lower()
        if user_answer == answers[i]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")

# Provide final score
    print("\nQuiz completed!")
    print(f"You got {score}/{len(questions)} questions correct.")

# Run the quiz function
quiz()
