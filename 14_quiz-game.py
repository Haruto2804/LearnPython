# The questions for the quiz (Stored in a tuple)
questions = (
    "What is the capital of France?",
    "Which planet is known as the Red Planet?",
    "What is the largest mammal on Earth?",
    "How many elements are in the periodic table?",
    "What year did the Titanic sink?"
)

# Options for each question (Tuple of tuples)
options = (
    ("A. Berlin", "B. Madrid", "C. Paris", "D. Rome"),
    ("A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"),
    ("A. Elephant", "B. Blue Whale", "C. Giraffe", "D. Shark"),
    ("A. 92", "B. 108", "C. 118", "D. 126"),
    ("A. 1912", "B. 1922", "C. 1905", "D. 1930")
)

# The correct answers
answers = ("C", "B", "B", "C", "A")

# Game tracking variables
guesses = []
score = 0
question_num = 0  

# Main Game Loop
for question in questions:
    print("-------------------------")
    print(question)
    
    for option in options[question_num]:
        print(option)
        
    # .upper() giúp tự động chuyển chữ thường thành chữ hoa (ví dụ: a -> A)
    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!!!")
    else:
        print(f"INCORRECT!! The correct answer was {answers[question_num]}.")
        
    question_num += 1

# --- RESULTS SECTION ---
print("-------------------------")
print("---------RESULTS---------")
print("-------------------------")

# Hiển thị danh sách đáp án đúng
print("Answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

# Hiển thị danh sách câu trả lời của người chơi
print("Guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

# Tính toán và hiển thị điểm số cuối cùng
final_score = int((score / len(questions)) * 100)
print(f"\nFinal Score: {final_score}% ({score}/{len(questions)})")