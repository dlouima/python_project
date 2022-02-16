from turtle import Screen, right
from paddle import Paddle


screen = Screen()
screen.setup(800, 600)
screen.bgcolor('black')
screen.title('Pong Game')
screen.tracer(0)
l_position = (370, 0)
r_position = (-380, 0)
left_paddle = Paddle(l_position)
right_paddle = Paddle(r_position)


screen.listen()
screen.onkeyrelease(left_paddle.up, 'Up')
screen.onkeyrelease(left_paddle.down, 'Down')

screen.onkeyrelease(right_paddle.up, 'w')
screen.onkeyrelease(right_paddle.down, 's')


game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()
