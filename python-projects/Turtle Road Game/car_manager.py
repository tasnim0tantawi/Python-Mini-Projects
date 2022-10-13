from turtle import Turtle
import random

COLORES = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "white"]
START_MOVE_DISTANCE = 4
MOVE_INCREMENT = 1


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = START_MOVE_DISTANCE

    def create_car(self):
        chance = random.randint(0, 6)
        if chance == 0:
            car = Turtle("square")
            car.penup()
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(random.choice(COLORES))
            random_y = random.randint(-300, 300)
            car.goto(300, random_y)
            self.all_cars.append(car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        for car in self.all_cars:
            self.car_speed += MOVE_INCREMENT
