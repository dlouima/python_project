from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.all_cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        number_of_car = random.randint(1, 6)
        if number_of_car == 1:
            car = Turtle('square')

            car.penup()
            car.color(random.choice(COLORS))
            car.shapesize(stretch_wid=1, stretch_len=3)
            car.goto(300, random.randint(-250, 250))
            self.all_cars.append(car)

    def move_car(self):
        for car in self.all_cars:
            car.back(self.speed)

    def spee_up(self):
        self.speed + MOVE_INCREMENT

    def reflesh(self):
        self.clear()
        self.create_car()
