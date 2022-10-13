import math


# An argument to the function is the actual input we pass to the function
# The parameter is the variable inside the definition of the function
# name is a parameter
def greet(name, location):
    print("Hello, " + name)
    print("You are in " + location)


# "Tasnim" is the argument
# Positional argument
greet("Tasnim", "Bahrain")
# Keyword argument
greet(name="Tasnim", location="Bahrain")
greet(location="Cairo", name="Mariam")

print("Cans exercise")


# Cans exercise


def cans(height, width, coverage):
    cans = math.ceil(((height * width) / coverage))
    return cans


wall_height = int(input("Enter the height of the wall: "))
wall_width = int(input("Enter the width of the wall: "))
wall_coverage = int(input("Enter the coverage of the can: "))
result = cans(wall_height, wall_width, wall_coverage)
print("The number of cans is: " + str(result))


# Prime number checker


def prime(number):
    if number == 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


is_prime = prime(int(input("Enter a number: ")))
if is_prime:
    print("The number is prime")
else:
    print("The number is not prime")


# Caesar cipher

def caesar_cipher(message, shift, encrypt):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
                "v", "w", "x", "y", "z"]
    encrypt = encrypt.lower()
    message = message.lower()
    new_message = ""
    if encrypt == "encode":
        for letter in message:
            new_message += alphabet[(alphabet.index(letter) + shift) % 26]
    elif encrypt == "decode":
        for letter in message:
            if letter in alphabet:
                new_message += alphabet[(alphabet.index(letter) - shift) % 26]
            else:
                new_message += letter
    return new_message


print("Caesar cipher")
encryption = input("Do you want to encode or decode? ")
msg = input("Enter a message: ")
shift_amount = int(input("Enter the shift: "))
repeat = ""
while True:
    print("The message is " + caesar_cipher(msg, shift_amount, encryption))
    repeat = input("Do you want to repeat? (yes/no) ").lower()
    if repeat == "yes":
        msg = input("Enter a message: ")
        shift_amount = int(input("Enter the shift: "))
        encryption = input("Do you want to encode or decode? ")
    else:
        break
