import time
from turtle import Screen
from player import FINISH_LINE_Y, Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
Scoreboard = Scoreboard()
car = CarManager()
player = Player()
screen.listen()
screen.onkeypress(player.move, 'Up')
screen.onkeypress(player.down, 'Down')


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_car()

    # detect collission with the car
    for i in car.all_cars:
        if i.distance(player) < 20:
            game_is_on = False
            Scoreboard.game_over()

    # detect when the turtle is successfully cross the road

    if player.ycor() > FINISH_LINE_Y:
        player.go_to_start()
        Scoreboard.increase_score()
        car.spee_up()

screen.exitonclick()
