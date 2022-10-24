from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5

class CarManager:
    def __init__(self):
        self.cars = []
        self.moving_speed = STARTING_MOVE_DISTANCE

    def create(self):
        coloring = random.choice(COLORS)
        car = Turtle("square")
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.color(coloring)
        car.seth(180)
        car.penup()
        car.goto(280, random.randint(-250, 250))
        self.cars.append(car)

    def move(self):
        for car in self.cars:
            car.forward(self.moving_speed)

    def level_up(self):
        self.moving_speed += MOVE_INCREMENT







