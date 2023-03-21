from turtle import Turtle
import random
from scoreboard import CURRENT_LEVEL

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
CAR_SPAWNS = ((300, -250), (300, -225), (300, -200), (300, -175), (300, -150), (300, -125), (300, -100), (300, -75),
              (300, -50), (300, -25), (300, 00), (300, 25), (300, 50), (300, 75), (300, 100), (300, 125), (300, 150),
            (300, 175), (300, 200))
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):
    def __init__(self):
        self.all_cars = []
        self.move_speed = STARTING_MOVE_DISTANCE

    def spawn_cars(self):
        new_car = Turtle()
        new_car.shape("square")
        new_car.shapesize(1, 2)
        new_car.penup()
        new_car.color(random.choice(COLORS))
        new_car.goto(random.choice(CAR_SPAWNS))
        self.all_cars.append(new_car)


    def move_cars(self):
        for cars in self.all_cars:
            cars.backward(self.move_speed + (self.move_speed * CURRENT_LEVEL))


    def clear_cars(self):
        for cars in self.all_cars:
            cars.hideturtle()
        self.all_cars.clear()


