import random
import colorgram
import turtle
from turtle import Turtle, Screen

# import turtle as t
# timmy = t.Turtle()
screen = Screen()
screen.bgcolor("Black")
timmy = Turtle()
timmy.color("coral")
timmy.shape("turtle")
colors = ["red", "green", "blue", "yellow", "orange", "purple", "pink", "white", "coral", "magenta", "cyan", "lime",
          "teal", "navy", "brown", "maroon", "olive", "silver", "gold", "gray", "indigo", "violet"]
directions = [0, 90, 180, 270]
# Draw a square
for i in range(4):
    timmy.forward(50)
    timmy.penup()
    timmy.forward(50)
    timmy.pendown()
    timmy.left(90)
timmy.pendown()
timmy.clear()


def draw_shape(sides):
    for i in range(sides):
        timmy.forward(50)
        timmy.left(360 / sides)


for i in range(3, 10):
    draw_shape(i)
    timmy.color(random.choice(colors))
timmy.clear()
timmy.width(10)
timmy.speed("fastest")
for _ in range(200):
    timmy.color(random.choice(colors))
    timmy.forward(30)
    timmy.setheading(random.choice(directions))

turtle.colormode(255)


def generate_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


timmy.setposition(0, 0)
timmy.clear()


def draw_circles(size_of_gap):
    for _ in range(360 // size_of_gap):
        timmy.color(generate_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)


draw_circles(10)
# colors = colorgram.extract_colors(screen.getcanvas())
# rgb_colors = []
# for color in colors:
    # r = color.rgb.r
    # g = color.rgb.g
    # b = color.rgb.b
    # new_color = (r, g, b)
    # rgb_colors.append(new_color)

number_of_dots = 100
timmy.clear()
timmy.penup()
timmy.hideturtle()
timmy.setheading(0)
timmy.setposition(-200, -200)
for i in range(1, number_of_dots+1):
    timmy.dot(20, random.choice(colors))
    timmy.forward(50)
    if i % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)

screen.exitonclick()
