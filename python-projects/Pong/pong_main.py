from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard_pong import Scoreboard
import time
# 1. Create the screen
screen = Screen()
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
screen.setup(width=800, height=600)
# 2. Create and move the paddle
paddle_right = Paddle(350, 0)
# 3. Create a second paddle
paddle_left = Paddle(-350, 0)
# 4. Create a ball
ball = Ball()
screen.listen()
screen.onkey(paddle_left.paddle_up, "w")
screen.onkey(paddle_left.paddle_down, "s")
screen.onkey(paddle_right.paddle_up, "Up")
screen.onkey(paddle_right.paddle_down, "Down")
scoreboard = Scoreboard()

is_on = True
while is_on:
    screen.update()
    # 4. Create a ball and move it around
    time.sleep(ball.move_speed)
    ball.move()
    # 5. Detect a collision between the ball and wall
    ball.bounce_y()
    # 6. Detect a collision between the ball and paddle and reverse the ball's direction
    if ball.xcor() > 320 and ball.distance(paddle_right) < 60 or ball.xcor() < -320 and ball.distance(paddle_left) <60:
        ball.bounce_x()
    # 7. Detect when the ball misses
    if ball.xcor() > 380:
        scoreboard.score_l_up()
        ball.reset()
    if ball.xcor() < -380:
        scoreboard.score_r_up()
        ball.reset()
# 8. Keep score

