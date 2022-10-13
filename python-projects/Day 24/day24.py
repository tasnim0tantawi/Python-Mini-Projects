# file = open("file.txt")
# contents = file.read()
# print(contents)
# file.close()
with open("file.txt", mode="w") as file:
    file.write("Hello World")
    # if the file doesn't exist, it will be created

with open("file.txt") as file:
    # with keyword is used to open the file and close it automatically
    contents = file.read()
    print(contents)

with open("file.txt", mode="a") as file:
    # append mode will add to the end of the file
    file.write("\nHello World again")


