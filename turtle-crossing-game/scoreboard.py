
from posixpath import supports_unicode_filenames
from turtle import Turtle
import turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.penup()
        self.hideturtle()
        self.score = 0
        self.reflesh_scoreboard()

    def reflesh_scoreboard(self):
        self.clear()
        self.goto(0, 260)
        self.write(f"Your Level { self.score}", align='center', font=FONT)

    def increase_score(self):
        self.score += 1
        self.reflesh_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over !", align='center', font=FONT)
