import random
import pandas
# List comprehension
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squared_numbers = [num**2 for num in numbers]
print(squared_numbers)

# List comprehension with if statement
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)

names = ["John", "Bob", "Mary", "Jane", "Jack", "Joe", "Tom", "Jerry", "Harry", "Mimosa", "Sally"]
capitalized_names = [name.upper() for name in names]
print(capitalized_names)

long_names = [name for name in names if len(name) > 4]
print(long_names)

with open("file1.txt") as file1:
    lines1 = file1.readlines()
with open("file2.txt") as file2:
    lines2 = file2.readlines()
result = [int(num) for num in lines1 if num in lines2]
print(result)

# Dictionary comprehension
# Create a dictionary from an existing list names
student_scores = {name: random.randint(1, 100) for name in names}
print(student_scores)

passed_students = {name: score for (name, score) in student_scores.items() if score >= 60}
sentence = "Love what you do, believe in yourself, and you'll be a winner."
count_letters = {word:len(word) for word in sentence.split()}
print(count_letters)
weather_daily ={
    "Monday": 40,
    "Tuesday": 30,
    "Wednesday": 25,
    "Thursday": 27,
    "Friday": 28,
    "Saturday": 30,
    "Sunday": 35
}
weather_f = {day: temp * 9/5 + 32 for (day, temp) in weather_daily.items()}
print(weather_f)
# We can loop through a dataframe the same way we loop through a dictionary
student_scores = {"Student": ["John", "Bob", "Mary", "Jane", "Jack", "Joe", "Tom", "Jerry", "Harry", "Mimosa", "Sally"],
                  "Score": [12, 34, 56, 78, 90, 12, 34, 56, 78, 90, 12]}
student_grades_df = pandas.DataFrame(student_scores)
print(student_grades_df)
# Loop through rows in the dataframe
for (index, row) in student_grades_df.iterrows():
    if row["Score"] >= 60:
        print(row["Student"])



