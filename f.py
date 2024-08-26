# Defining the questions as tuples with the question, answer options, and correct answer
questions = [
    ("What is the capital city of Kenya?", ["A. Mogadishu", "B. Nairobi", "C. Cairo", "D. Kigali"], "B"),
    ("What is the largest country in the world?", ["A. Seychelles", "B. Canada", "C. Russia", "D. Japan"], "C"),
    ("Which city hosts the EAC Headquarters?", ["A. Kampala", "B. Mombasa", "C. Nakuru", "D. Arusha"], "D"),
    ("What is the smallest planet in our solar system?", ["A. Earth", "B. Mars", "C. Mercury", "D. Jupiter"], "C"),
    ("Which sport is Kenya known for at the Olympics?", ["A. Athletics", "B. Swimming", "C. Gymnastics", "D. Golf"], "A")
]

# Defining a function to ask a single question and return whether the answer is correct or not
def ask_question(question, options, answer):
    print("\n" + question)
    for option in options:
        print(option)
    user_answer = input("Enter your answer (A/B/C/D): ")
    if user_answer.upper() == answer:
        print("Correct!")
        return 1
    else:
        print("Incorrect!")
        return 0

# Defining the main game function that asks all the questions, keeps score, and prints the final result
def quiz_game():
    print("Welcome to Collins' Python Project Quiz Game!")
    print("You will be asked 5 multiple-choice questions. Select an answer (A/B/C/D) for each question.")
    score = 0
    for question in questions:
        validated = False
        while not validated:
            validated = True
            score += ask_question(question[0], question[1], question[2])
            if score < 0 or score > len(questions):
                print("Error: Invalid score detected.")
                score = 0
                validated = False
    print(f"\nYou scored {score} out of {len(questions)}!")
    if score >= 3:
        print("Congratulations! You won!")
    else:
        print("Sorry, you lost. Better luck next time.")

# Call the main game function to run the quiz
quiz_game()




