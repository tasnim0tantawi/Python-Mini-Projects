from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("white")
        self.penup()
        self.reset()
        self.setheading(90)

    def up(self):
        self.forward(MOVE_DISTANCE)

    def finish(self):
        if self.ycor() > FINISH_Y:
            return True
        else:
            return False

    def reset(self):
        self.goto(STARTING_POSITION)



