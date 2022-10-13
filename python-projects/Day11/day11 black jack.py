import random
from os import system

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
keep = True


def sum(list):
    summation = 0
    for card in list:
        summation += card
    return summation


def win(user, computer):
    if user == computer:
        return "Tie"
    elif computer > 21 and user > 21:
        return "Tie"
    elif computer == 21:
        return False
    elif computer <= 21 and user > 21:
        return False
    elif user > computer and user <= 21:
        return True
    elif computer > 21:
        return True
    else:
        return False


def game():
    i = 2
    user = [random.choice(cards), random.choice(cards)]
    computer = [random.choice(cards), random.choice(cards)]
    total_user = sum(user)

    print(f"Your cards: {user}, current score is {total_user} ")
    print(f"Computer's first card: [{computer[0]} ,X] ")

    if sum(computer) < 17 and sum(computer != 21):
        computer.append(random.choice(cards))

    add = True
    while add and sum(computer) != 21 and sum(user) < 21:
        choice = input("Type 'y' to get another card, 'n' to pass:").lower()
        if choice == "y":
            user.append(random.choice(cards))
            if user[i] == 11 and sum(user) > 21:
                user[i] = 1
            i += 1
            print(f"Current Score: {sum(user)}, cards: {user}")
        else:
            add = False

    if win(sum(user), sum(computer)) == "Tie":
        print(
            f"Tie! Your total score is {sum(user)}, cards: {user}, Computer total is: {sum(computer)} cards: {computer}.")
    elif win(sum(user), sum(computer)):
        print(
            f"You win! Your total score is {sum(user)}, cards: {user}, Computer total is: {sum(computer)} cards: {computer}.")
    else:
        print(
            f"You lose! Your total score is {sum(user)}, cards: {user}, Computer total is: {sum(computer)} cards: {computer}.")


while keep:
    start = input("Do you want to play BlackJack game? Type 'y' or 'n': ").lower()
    if start == "n":
        keep = False
    system("clear")
    game()

