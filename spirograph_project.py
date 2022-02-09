import random
import turtle

circle = turtle.Turtle()
screen = turtle.Screen()

circle.speed('fastest')

def random_color():
    turtle.colormode(255)
    R = random.randint(0, 255)
    G = random.randint(0, 255)
    B = random.randint(0, 255)
    circle.color(R, G, B)

for angle in range(360):
    if angle % 5 == 0:
        circle.setheading(angle)
        random_color()
        circle.circle(90)

screen.exitonclick()