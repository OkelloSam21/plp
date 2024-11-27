#!/usr/bin/env python3

print("Welcome to the quiz")

questions = [
        "What is the keyword to define a function in python? ",
        "who directed the movie 'inception'? ",
        "what is the capital of Kenya? "
        ]

choices = [
        ["1. function", "2. def", "3.func", "4. lambda"],
        ["1. Quentin Taratino", "2. Christopher Nolan", "3. Steven Spielberg", "4. Martin Scorses"],
        ["1. Madrid", "2. Cairo", "3. Kisumu", "4.Nairobi"]
        ]

correct_answers = [2,2,4]

play_again = "yes"

while play_again == "yes":
    score = 0

    for i in range(len(questions)):
        print(f"\nQ{i+1}: {questions[i]}")
        for choice in choices[i]:
            print(choice)
        
        answer = int(input("Enter the number of your answer: "))

        if answer == correct_answers[i]:
            print("correct!")
            score += 1
        else:
            print("Wrong! the correct answer was: {choices[i][correct_answers[i] -1]")


    print(f"\nYou got {score} out of {len(questions)} questions right!")

    play_again = input("\nDo you want to play again? (yes/no): ").lower()

print("Thanks for playing! goodbye!")
