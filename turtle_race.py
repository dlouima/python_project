import random
from tokenize import Pointfloat
from turtle import Turtle, Screen, color, position

screen = Screen()
screen.setup(width=500, height=400)
is_race_on = False
colors = ['red', 'orange', 'green', 'blue', 'purple', 'yellow']
y_position = [-100, -50, 0, 50, 100, 150]
all_turtles = []

user_bit = screen.textinput(
    title='Make your bit', prompt='which turtle will win the race ? Enter a color: ')


for turtle in range(0, 6):
    pipo = Turtle(shape='turtle')
    pipo.color(colors[turtle])
    pipo.penup()
    pipo.goto(-230, y_position[turtle])
    pipo.goto(x=-230, y=y_position[turtle])
    all_turtles.append(pipo)

if user_bit:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        # 230 is 250 - half the width of the turtle.
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bit:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(
                    f"You've lost! The {winning_color} turtle is the winner!")

        # Make each turtle move a random amount.
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()
