def load_questions(filename):
    questions = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                # Split each line into question and answer at the '|' delimiter
                question, answer = line.strip().split('|')
                questions.append((question, answer))
    except FileNotFoundError:
        print(f"Error: '{filename}' not found. Please ensure the file exists.")
        return []
    except ValueError:
        print("Error: File format is incorrect. Each line should be 'question|answer'.")
        return []
    return questions


def run_quiz(questions):
    if not questions:
        print("No questions available to run the quiz.")
        return

    score = 0
    total = len(questions)
    print(f"\nWelcome to the Cricket Quiz! There are {total} questions.\n")

    for i, (question, correct_answer) in enumerate(questions, 1):
        print(f"Question {i}: {question}")
        user_answer = input("Your answer: ").strip().lower()

        if user_answer == correct_answer.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was: {correct_answer}")
        print()

    percentage = (score / total) * 100
    print(f"Quiz complete! Your score: {score}/{total} ({percentage:.2f}%)")


def main():
    filename = "cricket_quiz.txt"
    questions = load_questions(filename)
    run_quiz(questions)


if __name__ == "__main__":
    main()