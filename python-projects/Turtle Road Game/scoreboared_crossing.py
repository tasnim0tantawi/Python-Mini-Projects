from turtle import Turtle

FONT = ("Courrier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-250, 250)
        self.color("white")
        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score = self.score + 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align="center", font=FONT)


