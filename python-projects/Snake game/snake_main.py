import time
from turtle import Screen
from snakeC import Snake
from scoreboard import Scoreboard
from food import Food
# Steps to build snake game:
# 1. Create a snake body
# 2. Move the snake
# 3. Create a random located food
# 4. Detect collision between snake and food and grow the snake
# 5. Create a scoreboard
# 6. Detect collision between snake and wall and game over
# 7. Detect collision between snake and itself and game over
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
segments = []
snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


screen.update()
game_is_on = True
# 2. Move the snake
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # Collision between snake and food
    if snake.head.distance(food) < 20:
        food.refresh()
        scoreboard.increase()
        snake.grow()
    # Collision between snake and wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset()
        snake.reset()
    # Collision between snake and itself
    # Checking if the head of the snake has a distance that is less than 10 from any of the segments

    for segment in segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()





screen.exitonclick()

