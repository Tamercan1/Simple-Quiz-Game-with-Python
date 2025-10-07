import requests
import html
import random

score = 0

while True:
    url = "https://opentdb.com/api.php?amount=10&category=22&difficulty=easy&type=multiple"
    response = requests.get(url)
    data = response.json()
    question_data = data["results"][0]

    question = html.unescape(question_data["question"])
    correct = html.unescape(question_data["correct_answer"])
    incorrect = [html.unescape(i) for i in question_data["incorrect_answers"]]

    options = [correct] + incorrect
    random.shuffle(options)

    print(f"\nQuestion: {question}")
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")

    ans = input("Enter the number of your choice (q to quit)\n>>> ")

    if ans.lower() == "q":
        print("Exiting..")
        break
    
    try:
        chosen = options[int(ans) - 1]
        if chosen == correct:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {correct}")
    except (ValueError, IndexError):
        print("Invalid choice. Please enter a valid number.")

print(f"you got {score} points")
