import time
from turtle import Screen
from Pong.player import Player
from car_manager import CarManager
from scoreboared_crossing import Scoreboard
# 1. Move the turtle forward with keypress
# 2. Create and move the cars randomly
# 3. Detect collision with cars
# 4. Detect when the turtle reaches the finish line
# 5. Create a scoreboard
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Crossing Turtle")
screen.tracer(0)
screen.listen()
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
screen.onkey(player.up, "Up")

is_on = True
while is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    for car in car_manager.all_cars:
        if car.distance(player) < 15:
            scoreboard.game_over()
            is_on = False
        if player.finish():
            scoreboard.increase_score()
            car_manager.level_up()
            player.reset()
screen.exitonclick()

