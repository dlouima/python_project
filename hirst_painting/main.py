import random
import turtle as t
t.colormode(255)

rgb_colors = [(234, 245, 250), (196, 9, 68), (244, 230, 74), (212, 155, 90), (19, 117, 174), (168, 169, 27), (107, 180, 209), (218, 131, 166), (163, 74, 30), (238, 72, 34), (5, 35, 87), (26, 139, 72), (124, 181, 142), (219, 76, 122), (240, 222, 3), (82, 17, 80), (175, 47, 90), (9, 59, 35), (12, 166, 213), (239, 160, 190), (126, 33, 21), (9, 44, 130), (52, 164, 114), (4, 104, 63), (4, 88, 99), (142, 209, 220), (100, 31, 13)]

siro = t.Turtle()
screen = t.Screen()
siro.speed('fastest')
siro.penup()
siro.hideturtle()

siro.setheading(225)
siro.forward(250)
siro.setheading(0)
number_of_dot = 100

for dot in range(1, number_of_dot+1):
    siro.dot(20, random.choice(rgb_colors) )
    siro.forward(50)
    if dot % 10 == 0:
        siro.setheading(90)
        siro.forward(50)
        siro.setheading(180)
        siro.forward(500)
        siro.setheading(0)


screen.exitonclick()
