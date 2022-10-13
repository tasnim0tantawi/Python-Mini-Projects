import turtle
import pandas
from turtle import Turtle, Screen
screen = Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
turtle.penup()

data = pandas.read_csv("50_states.csv")
state_names = data["state"].tolist()
guessed_states = []
missed_states = []

while len(guessed_states) < 50:
    answer = screen.textinput(title=f"US States Game | {len(guessed_states)}/50", prompt="Guess a state?").title()
    if answer == "Exit":
        for state in state_names:
            if state not in guessed_states:
                missed_states.append(state)
        new_data = pandas.DataFrame(missed_states)
        new_data.to_csv("missed_states.csv")
        break
    if answer in state_names:
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        state_data = data[data["state"] == answer]
        t.goto(int(state_data["x"]), int(state_data["y"]))
        t.write(answer, font=("Arial", 10, "normal"))
        guessed_states.append(answer)

screen.exitonclick()







