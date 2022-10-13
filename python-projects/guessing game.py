import random
from random import randint

print("Welcome to the game of guessing a number!")
number = random.randint(1, 100)
difficulty = input("Choose a difficulty: \n "
                   "easy, medium, hard: ").lower()
guess = int(input("Guess a number between 1 and 100: "))

if difficulty == "easy":
    lives = 10
elif difficulty == "medium":
    lives = 7
elif difficulty == "hard":
    lives = 5
print(f"You have {lives} attempts to guess.")

while guess != number and lives > 0:
    if guess > number:
        print("Too high")
        lives -= 1
        print(f"You have {lives} attempts to guess.")
    elif guess < number:
        print("Too low")
        lives -= 1
        print(f"You have {lives} attempts to guess.")
    guess = int(input("Guess again: "))
    if lives == 0:
        print("You lost!")
        print("The number was:", number)

if lives > 0:
    print("You won!")

# Angela's solution

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


# Function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
    """checks answer against guess. Returns the number of turns remaining."""
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")


# Make function to set difficulty.
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    # Choosing a random number between 1 and 100.
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    print(f"Pssst, the correct answer is {answer}")

    turns = set_difficulty()
    # Repeat the guessing functionality if they get it wrong.
    guess_ang = 0
    while guess_ang != answer:
        print(f"You have {turns} attempts remaining to guess the number.")

        # Let the user guess a number.
        guess_ang = int(input("Make a guess: "))

        # Track the number of turns and reduce by 1 if they get it wrong.
        turns = check_answer(guess_ang, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess_ang != answer:
            print("Guess again.")


game()
