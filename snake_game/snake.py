from turtle import Turtle, position


start_postion = [(0, 0), (-20, 0), (-40, 0)]


class Snake():
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self,):
        for start in start_postion:
            self.create_segment(start)

    def create_segment(self, start):
        section = Turtle(shape='square')
        section.penup()
        section.color('white')
        section.goto(start)
        self.segments.append(section)

    def extend(self):
        self.create_segment(self.segments[-1].position())

    def move(self):
        for seg_position in range(len(self.segments)-1, 0, -1):
            x_coordinate = self.segments[seg_position-1].xcor()
            y_coordinate = self.segments[seg_position-1].ycor()
            self.segments[seg_position].goto(x_coordinate, y_coordinate)
        self.head.forward(20)

    def move_up(self):
        for snake in self.segments:
            if self.head.heading() != 270:
                self.head.setheading(90)

    def move_right(self):
        for snake in self.segments:
            if self.head.heading() != 180:
                self.head.setheading(0)

    def move_left(self):
        for snake in self.segments:
            if self.head.heading() != 0:
                self.head.setheading(180)

    def move_down(self):
        for snake in self.segments:
            if self.head.heading() != 90:
                self.head.setheading(270)
