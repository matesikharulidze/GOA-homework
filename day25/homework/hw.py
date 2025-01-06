import random

def guess_the_number():
    print("Think of a number between 1 and 100.")
    print("I will try to guess it within 3 attempts!")
    
    low = 1
    high = 100
    attempts = 3

    for attempt in range(1, attempts + 1):
        # კომპიუტერი აკეთებს გამოცნობას
        guess = random.randint(low, high)
        print(f"\nAttempt {attempt}: Is your number {guess}?")
        
        # მომხმარებლის რეაქციის კითხვა
        feedback = input("Type 'higher', 'lower', or 'correct': ").lower()
        
        if feedback == "higher":
            low = guess + 1  # რიცხვი უფრო მაღალია, დიაპაზონი მცირდება
        elif feedback == "lower":
            high = guess - 1  # რიცხვი უფრო დაბალია, დიაპაზონი მცირდება
        elif feedback == "correct":
            print(f"\nGreat! I guessed your number {guess} in {attempt} attempts!")
            break
        else:
            print("Invalid input. Please type 'higher', 'lower', or 'correct'.")
            continue
        
        if attempt == attempts:
            print("\nI'm out of attempts! Better luck next time!")
            break

# თამაში
guess_the_number()
