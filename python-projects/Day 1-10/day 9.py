from os import system

# Dictionaries
# Key: Value
dict1 = {"Bug": "An error in the program", "Buggy": "A program that has an error"}
# Bug is the key
# An error in the program is the value
# Dictionaries are similar to JSON
# They are built on the idea of hash table data structure

# Adding a new key-value pair to a dictionary
dict1["Loop"] = "A loop is a way to repeat a block of code"

# retrieving a value from a dictionary
print(dict1["Loop"])

# Clearing a dictionary
# dict1.clear()

# Creating an empty dictionary
dict2 = {}

# Editing a value in a dictionary
dict1["Bug"] = "An error in the program that prevents it from running as expected"

# Looping through a dictionary
for key in dict1:
    # Printing the key
    print(key)
    # Printing the value
    print(dict1[key])

students_grades = {}
student_scores = {"Tasnim": 100, "Mariam": 95, "Sara": 70, "Ahmed": 40, "Ali": 90, "Hermione": 99}
for key in student_scores:
    if student_scores[key] >= 90:
        students_grades[key] = "A"
    elif student_scores[key] >= 80:
        students_grades[key] = "B"
    elif student_scores[key] >= 70:
        students_grades[key] = "C"
    elif student_scores[key] >= 60:
        students_grades[key] = "D"
    else:
        students_grades[key] = "F"

# Nesting a list inside a dictionary
travel_log = {"Tasnim": ["Bahrain", "Cairo", "Dubai"],
              "Mariam": ["Paris", "London", "New York"],
              "Sara": ["Berlin", "New York", "Hamburg"]}
# Nesting a dictionary inside a dictionary
travel_log2 = {"Tasnim":
                   {"Cities visited": ["Bahrain", "Cairo", "Dubai"],
                    "Total visits": 5
                    },
               "Mariam":
                   {"Cities visited": ["Paris", "London", "New York"],
                    "Total visits": 4},
               "Sara":
                   {"Cities visited": ["Berlin", "New York", "Hamburg"],
                    "Total visits": 3}
               }
# Secret Auction
print("Welcome to the Secret Auction")
is_on = True
bids = {}
name = input("Enter your name: ")
bid = float(input("Enter your bid: "))
bids[name] = bid
while is_on:
    keep = input("Is there another bidders? (yes/no): ").lower()
    if keep == "no":
        is_on = False
    else:
        system("clear")
        name = input("Enter your name: ")
        bid = float(input("Enter your bid $: "))
        bids[name] = bid

max = 0
for name in bids:
    if bids[name] > max:
        max = bids[name]
        winner = name
print("The winner is: " + winner + " with a bid of: " + str(max))


def format_name(first, last):
    # Formatting a string
    if first == "" or last == "":
        return
    proper_name = first.title() + " " + last.title()
    return proper_name


def leap_year(year):
    """
    Returns True if year is a leap year.
    This is a documentation string that describes what the function does.
    """
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(month, year):
    """
    Returns the number of days in a month.
    """
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if leap_year(year):
        days_in_month[1] = 29
    else:
        days_in_month[1] = 28
    return days_in_month[month - 1]


result3 = days_in_month(int(input("Enter a month: ")), int(input("Enter a year: ")))


def add_numbers(num1, num2):
    """
    Returns the sum of two numbers.
    """
    return num1 + num2


def subtract_numbers(num1, num2):
    """
    Returns the difference of two numbers.
    """
    return num1 - num2


def multiply_numbers(num1, num2):
    """
    Returns the product of two numbers.
    """
    return num1 * num2


def divide_numbers(num1, num2):
    """
    Returns the quotient of two numbers.
    """
    return num1 / num2

operations = {
        "+": add_numbers,
        "-": subtract_numbers,
        "*": multiply_numbers,
        "/": divide_numbers
    }


def calculator():
    is_on = True
    num1 = float(input("Enter a number: "))
    while is_on:
        num2 = float(input("Enter another number: "))
        operation = input("Enter an operation: ")
        for symbol in operations:
            print(symbol)
        calc_function = operations[operation]
        result = calc_function(num1, num2)
        print(num1 + " " + operation + " " + str(num2) + " = " + str(result))
        keep = input("Do you want to do another calculation? (yes/no): ").lower()
        if keep == "no":
            calculator()
        else:
            num1 = result
            system("clear")
            print(result)
            

