from turtle import Turtle, Screen
from random import randint
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("coral")
        self.penup()
        self.shapesize(stretch_len=0.6, stretch_wid=0.6)
        self.speed(0)
        self.speed = "fastest"
        self.refresh()
    def refresh(self):
        self.goto(randint(-280, 280), randint(-280, 280))


