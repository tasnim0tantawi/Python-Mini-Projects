try:
    file = open("a_file.txt", "r")
    a_dict = {"English": "Hello", "Spanish": "Hola", "French": "Bonjour", "German": "Hallo"}
    print(a_dict["Japanese"])
except FileNotFoundError:
    print("File not found! Creating a new file...")
    file = open("a_file.txt", "w")
    file.write("This is a test file!")
    file = open("data.txt", "r")
except KeyError as e:
    print(f"{e} Key not found!")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File closed!")
# raise KeyError("This is an error I made up!")

height = int(input("Enter your height in inches: "))
weight = int(input("Enter your weight in pounds: "))
if height > 3:
    raise ValueError("Height must be less than 3m!")
bmi = weight / (height * height)



