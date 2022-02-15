from turtle import Turtle, pos, turtles
from typing import Tuple
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('yellow')
        self.speed('fastest')
        self.penup()
        self.shapesize(0.6, 0.6)
        self.screen_reflesh()

    def screen_reflesh(self):
        x = random.randint(-278, 278)
        y = random.randint(-278, 278)
        self.goto(x, y)
