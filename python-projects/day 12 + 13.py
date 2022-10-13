# Scope
# Internal Scope
def example_internal():
    # x is a local variable, cannot be accessed outside of the function
    x = 10

    # function ex is a local function, cannot be called outside this function
    def ex():
        print(x)

    ex()


# Global Scope
# Global variables can be accessed everywhere in the program
y = 19

# In python, there is no block scope.
# means that variables inside loops and if statements can be accessed outside of the loop and if statement.
# Scope works in functions.
game_level = 3
monsters = ["Goblin", "Orc", "Troll"]
if game_level < 5:
    monster = monsters[0]
print(monster)
# monster variable is accessible outside the if statement

enemies = 1


def example_global():
    """
    This function will modify the global variable enemies
    """
    # It is a bad practice to modify global variables inside a function
    global enemies
    enemies += 2
    print(enemies)

# Debugging
# 1. Describe the problem
# 2. Reproduce the bug  to notice when and why it happens
# 3. Play computer, trace the code
# 4. Fix the error before you continue
# 5. Use print statements to help you debug
# 6. Use the debugger to help you debug
# 7. Take a break
# 8. Ask for help


