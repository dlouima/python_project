from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('black')
        self.penup()
        self.go_to_start()
        self.setheading(90)

    def move(self):
        self.forward(20)

    def down(self):
        new_x = self.xcor()
        new_y = self.ycor()-MOVE_DISTANCE
        self.goto(new_x, new_y)

    def go_to_start(self):
        self.goto(STARTING_POSITION)
