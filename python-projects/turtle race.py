from turtle import Turtle, Screen
import random
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
screen = Screen()
screen.setup(width=500, height=400)

is_on = False
turtles = []

user_bet = screen.textinput(title="Make your bet:", prompt="Which turtle will wu=in the race?")
if user_bet:
    is_on = True

for i in range(6):
    timmy = Turtle()
    timmy.color(colors[i])
    timmy.shape("turtle")
    timmy.penup()
    timmy.goto(-220, y_positions[i])
    turtles.append(timmy)
while is_on:
    for timmy in turtles:
        rand_speed = random.randint(1, 10)
        timmy.forward(rand_speed)
        if timmy.xcor() >= 220:
            win = timmy.pencolor()
            is_on = False
            if win == user_bet:
                screen.textinput(title="You win!", prompt="You win!")
            else:
                screen.textinput(title="You lose!", prompt="You lose!")
            break


screen.exitonclick()