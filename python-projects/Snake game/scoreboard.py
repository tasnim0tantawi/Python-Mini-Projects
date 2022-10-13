from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as f:
            self.highscore = int(f.read())
        self.penup()
        self.hideturtle()
        self.goto(-230, 250)
        self.color("white")
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score: {self.score} | High Score: {self.highscore}", False, align="left",
                   font=("Arial", 14, "normal"))

    def increase(self):
        self.score += 1
        self.update()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            open("data.txt", "w").write(str(self.highscore))
        self.score = 0
        self.update()
