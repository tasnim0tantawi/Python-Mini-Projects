from follower_data import data
import random
from os import system

logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""
is_on = True
showed = []
score = 0
a = random.choice(data)

while is_on:
    b = random.choice(data)
    while a == b:
        b = random.choice(data)
    while b in showed:
        b = random.choice(data)

    showed.append(a)
    showed.append(b)
    print(logo)
    print(f"A: {a['name']}, a {a['description']} from {a['country']}")
    print(vs)
    print(f"B: {b['name']}, a {b['description']} from {b['country']}")
    guess = input(f"Guess the name of the person who has the most followers, A or B:").lower()
    correct = ""
    if a['follower_count'] > b['follower_count']:
        correct_answer = 'a'
        correct = a
    else:
        correct = b
        correct_answer = 'b'
    if guess == correct_answer:
        system('cls')
        print("Correct! Your current score is: ", score)
        a = correct
        score += 1
    else:
        system('cls')
        print("Wrong! Final score is: ", score)
        break




