print("Day 1")
print("Welcome to my silly system!\n First Program")
# Indentation in python is critical, indentationError happens when we don't properly indent code.
print("Band Name Generator")
name = input("What is your name? ")
pet = input("What is your pet name? ")
print(f"Your band name is: {name} {pet}")
# The above code is a string interpolation, it is a way to combine strings and variables.
# Ctrl + / to comment out a line of code.
print("_" * 20)
print(f"The number of characters in your band name is: {len(name) + len(pet)}")
pet, name = name, pet
print(f"The first character in your name is: {name[0]}")
print(f"The first character in your pet name is: {pet[0]}")

print("Day 2")
print("Welcome to the tip calculator\n Second Program")
bill = float(input("What was the total bill? "))
num_people = int(input("How many people you want to split the bill over? "))
tip = float(input("What is the tip percentage you want to give? "))
tip = (tip + 100) / 100
total = bill * tip
print(f"Each of you will pay: $ {round(total / num_people, 2)}")
mystery = 12_87_65_43_21  # This is a long number, we put the _ in front of the number to make it easier to read.
print(type(input("Checking the type of input: ")))
print(type(mystery))
print("_" * 20)

print("Simple calculator: Summation of digits")
num1 = input("What is the number?")
summ = 0
for i in num1:
    sum += int(i)
print(f"The sum of the digits in {num1} is {summ}")
print("_" * 20)
print("Simple calculator: Reverse a number")
num2 = input("What is the number?")
# num2 = num2[::-1]
for i in range(len(num2)):
    print(num2[len(num2) - i - 1])
print("_" * 20)
print("Mathematical operators")
print(f"Exponent: {2 ** 3}")
print(f"Square root: {2 ** 0.5}")
print(f"Division that returns float: {2 / 3}")
print(f"Division that returns int AKA floor division: {2 // 3}")
print(f"Approximation: {round(22 / 7, 2)}")
print(f"Approximation: {round(2.66666666666666666666667, 2)}")
# in Python. we cannot use count++
count = 0
count += 1
print("Life in weeks")
age = input("How old are you? ")
print(f"You have {(60 - int(age)) * 52} weeks left if you are going to live for 60 years.")
print(f"{(60 - int(age)) * 365} days left.")
print(f"{(60 - int(age)) * 365 * 24} hours left.")

print("Day 3")
print("Welcome to the Treasure Land\n Third Program")
# Ascii Art

direction = input("Which direction do you want to go? left, right? ").lower()
if direction == "right":
    print("Game over! You fell into a hole!")
else:
    swim = input("Do you want to swim or wait? ").lower()
    if swim == "swim":
        print("Game over! You are being chased by a shark!")
    else:
        door_color = input("What is the color of the door you want to choose? Red, blue, green? ").lower()
        if door_color == "red":
            print("Game over! You are in a trap!")
        elif door_color == "blue":
            print("Game over! You are in a room in fire!")
        else:
            print("You made it to the treasure land!")

print("_" * 20)
height = float(input("What is your height in cm? "))
age = int(input("What is your age? "))
photo = input("Do you want a photo? y/n ")
price = 0
if height >= 120:
    print("You are tall enough to ride the roller coaster!")
    if age < 12:
        price = 5
    elif 18 > age >= 12:
        price = 7
    elif 45 <= age <= 55:
        price = 0
    else:
        price = 14
    if photo == "y":
        price += 3
    print(f"You should pay ${price}")
else:
    print("Sorry! You too short to ride the roller coaster!")

print("_" * 20)
print("Leap Year Calculator")
year = int(input("What year is it? "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("It is a leap year!")
        else:
            print("It is not a leap year!")
    else:
        print("It is a leap year!")
else:
    print("Not a leap year")
print("_" * 20)
print("Love Calculator")
name1 = input("What is your name? ").lower()
crush = input("What is your crush's name? ").lower()
full = name1 + crush
count_love = 0
count_true = 0
count_love += full.count("l")
count_love += full.count("o")
count_love += full.count("v")
count_love += full.count("e")

count_true = full.count("t")
count_true += full.count("r")
count_true += full.count("u")
count_true += full.count("e")
percentage = int(str(count_love) + str(count_true))
print(f"{name1} and {crush} are {percentage}% compatible.")
if percentage > 90:
    print("You should be in a relationship!")
elif percentage > 50:
    print("You are okay together!")
else:
    print("You should be alone!")
print("_" * 20)

print("Day 4")
import random

# 🚨 Rock, Paper Scissors 👇
print("Welcome to Rock, Paper, Scissors!")
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
choices = [rock, paper, scissors]
choice = int(input("What do you want to choose? 0 for Rock, 1 for Paper, 2 for Scissors: "))
if choice < 0 or choice > 2:
    print("Invalid choice!")
else:
    if choice == 0:
        print("You chose rock: ")
        print(choices[choice])
    elif choice == 1:
        print("You chose paper: ")
        print(choices[choice])
    elif choice == 2:
        print("You chose scissors: ")
        print(choices[choice])

    computer_choice = random.randint(0, 2)

    if computer_choice == 0:
        print("Computer chose rock:")
        print(choices[computer_choice])
    elif computer_choice == 1:
        print("Computer chose paper")
        print(choices[computer_choice])
    elif computer_choice == 2:
        print("Computer chose scissors")
        print(choices[computer_choice])
    if choice == computer_choice:
        print("Tie!")
    elif choice == 0 and computer_choice == 1:
        print("You lose! ")
    elif choice == 0 and computer_choice == 2:
        print("You Win! ")
    elif choice == 1 and computer_choice == 0:
        print("You Win! ")
    elif choice == 1 and computer_choice == 2:
        print("You lose! ")
    elif choice == 2 and computer_choice == 0:
        print("You lose! ")
    elif choice == 2 and computer_choice == 1:
        print("You win! ")

# .randint(1, 10) is a function that generates a random number between 1 and 10.
random_number = random.randint(1, 10)
# .random() is a function that generates a random floating point number between 0 and 1.
random_decimal = random.random()
# To generate a random floating point number between 0 and 10, we need to multiply the random number by 10.
random_decimal = random.random() * 10
print(f"Random decimal: {random_decimal}")
print("_" * 20)
print("Python Lists")

fruits = ["Apple", "Banana", "Orange", "Pear"]
states = ["California", "Florida", "New York", "Texas", "Washington", "Oregon", "North Carolina"]
num_states = len(states)

# append() adds an element to the end of a list, while extend() adds a list to the list.
fruits.append("Strawberry")
states.extend(["Utah", "Hawaii"])
print("_" * 20)
print("Bill split exercise")
names = input("Enter all of your names separated by a comma: ")
names = names.split(",")
bad_luck = random.choice(names)
print(f"{bad_luck} is going to pay for you all!")
print("_" * 20)
# 🚨 Treasure Map 👇
print("Treasure Map Exercise")
row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
index = input("Where do you want to put the treasure? ")
row = int(index[0]) - 1
column = int(index[1]) - 1
map[row][column] = "X"
print(map)
print("_" * 20)


print("Day 5")
print("Welcome to password generator!")
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
           "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
           "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
special_characters = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "~", "`", "|"]
numbers_p = int(input("How many numbers you want in your password? "))
characters_p = int(input("How many characters you want in your password? "))
special_p = int(input("How many special characters you want in your password? "))
password = ""
for number in range(numbers_p):
    password += random.choice(numbers)
for character in range(characters_p):
    password += random.choice(letters)
for special in range(special_p):
    password += random.choice(special_characters)

password = password.split()
random.shuffle(password)
password = "".join(password)
print(f"Your password is: {password}")

# Summation of even numbers from 2 to 100
sum_even = 0
for i in range(2, 101, 2):
    sum_even += i
print(f"Sum of even numbers from 2 to 100: {sum_even}")
print("_" * 20)
print("Day 6")
# For loops are better when we want to iterate over a list or dictionary or any iterable object.
# While loops are better when we want to run a block of code a number of times as long as a condition is true.

