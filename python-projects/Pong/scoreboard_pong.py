from turtle import Turtle, Screen

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0, 180)
        self.color("white")
        self.score_a = 0
        self.score_b = 0
        self.update()

    def update(self):
        self.clear()
        self.write(f"{self.score_a} | {self.score_b}", align="center", font=("Courier", 80, "normal"))

    def score_l_up(self):
        self.score_a += 1
        self.update()

    def score_r_up(self):
        self.score_b += 1
        self.update()
    def reset(self):
        self.score_a = 0
        self.score_b = 0
        self.update()