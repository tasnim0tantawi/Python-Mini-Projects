from turtle import Turtle, Screen

# event listeners allows us to control the behavior of a turtle object
# higher order functions allow us to create functions that take other functions as arguments
# higher order functions are functions that take other functions as arguments
# some programming languages have higher order functions, like Python. Others don't.
# when we pass a function as an argument to another function, we remove the parentheses ()
# Etch a sketch:
timmy = Turtle()
timmy.color("coral")
screen = Screen()


def forward():
    timmy.forward(10)


def backward():
    timmy.backward(10)


def left():
    timmy.left(10)


def right():
    timmy.right(10)


def clear():
    timmy.clear()
    timmy.penup()
    timmy.goto(0, 0)
    timmy.pendown()


screen.listen()
screen.bgcolor("black")
screen.onkey(forward, "Up")
screen.onkey(backward, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")
screen.onkey(clear, "c")

screen.exitonclick()
