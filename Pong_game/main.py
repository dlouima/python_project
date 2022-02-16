from turtle import Screen, right
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(800, 600)
screen.bgcolor('black')
screen.title('Pong Game')
screen.tracer(0)
r_position = (370, 0)
l_position = (-380, 0)
left_paddle = Paddle(l_position)
right_paddle = Paddle(r_position)
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkeyrelease(left_paddle.up, 'w')
screen.onkeyrelease(left_paddle.down, 's')

screen.onkeyrelease(right_paddle.up, 'Up')
screen.onkeyrelease(right_paddle.down, 'Down')


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
# detect when the ball touch the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

        # when the touch the right paddle or the left paddle

    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        # detect when the ball miss the right paddle
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_score_point()
        # detect when the ball miss the left paddle
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_score_point()


screen.exitonclick()
