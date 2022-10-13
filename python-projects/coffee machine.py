# Program Requirements:
# 1. Print report
# 2. Check if resources are sufficient for the coffee
# 3. Process coins and return change
# 4. Check transaction successful
# 5. Make coffee
total_profit = 0
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_resources(ingredients):
    global resources
    for ingredient in ingredients:
        if resources[ingredient] < ingredients[ingredient]:
            print(f"Sorry, not enough {ingredient}!")
            return False
    return True


def calculate_cost(quarters, dimes, nickels, pennies, price):
    cost = 0
    cost += quarters * 0.25
    cost += dimes * 0.10
    cost += nickels * 0.05
    cost += pennies * 0.01
    if cost < price:
        print("Not enough money!")
        return False
    if cost > price:
        change = cost - price
    else:
        change = 0
    return cost, change


def print_report():
    global total_profit
    print("Water:", resources["water"])
    print("Milk:", resources["milk"])
    print("Coffee:", resources["coffee"])
    print("Change:", change)
    print("Total:", total_profit)
    print("Thank you!")


menu = ["espresso", "latte", "cappuccino"]

is_on = True
while is_on:
    choice = input("What do you want to choose? espresso, latte, or cappuccino: ").lower()
    if (choice not in menu) and (choice != "off" or choice != "report"):
        print(menu)
        continue
    if choice == "off":
        is_on = False
        print("Thank you!")
    elif choice == "report":
        print_report()
    else:
        drink = MENU[choice]
        if check_resources(drink["ingredients"]):
            quarters_input = int(input("Insert quarters: "))
            dimes_input = int(input("Insert dimes: "))
            nickels_input = int(input("Insert nickels: "))
            pennies_input = int(input("Insert pennies: "))
            price = MENU[choice]["cost"]
            cost, change = calculate_cost(quarters_input, dimes_input, nickels_input, pennies_input, price)
            change = round(change, 2)
            if cost:
                total_profit += cost
                for ingredient in drink["ingredients"]:
                    resources[ingredient] -= drink["ingredients"][ingredient]
                print("Your drink is ready!")
                print(f"Change: {change}")
            else:
                print("Not enough money! Money returned!")






