from turtle import Screen
import time
from snake import Snake
from food import Food
from sboreboard import Scoreboard


screen = Screen()
screen.title("The Snake Game")
screen.tracer(0)
screen.setup(600, 600)
screen.bgcolor('black')
score = Scoreboard()
food = Food()
snake = Snake()
screen.listen()
screen.onkeypress(snake.move_up, "Up")
screen.onkeypress(snake.move_down, "Down")
screen.onkeypress(snake.move_right, "Right")
screen.onkeypress(snake.move_left, "Left")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
# detect colision with food
    if snake.head.distance(food) < 15:
        food.screen_reflesh()
        score.increase_score()
        snake.extend()

# detect colosion with the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score.game_over()
        game_is_on = False

        # detect colision with taild
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            Scoreboard.game_over()


screen.exitonclick()
