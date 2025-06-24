print("Welcome to the quiz!")
questions = [
    {"question": "What is the capital of India?", "answer": "New Delhi"},
    {"question": "What is 2 + 2?", "answer": "4"},
    {"question": "Who wrote Harry Potter?", "answer": "J.K. Rowling"}
]

score = 0

for q in questions:
    user_answer = input(q["question"] + " ")
    if user_answer.strip()== q["answer"]:
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")

print("Your final score is", score, "out of 3.")