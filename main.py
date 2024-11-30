import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()


scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_cars()
    car.move_car()

    if player.ycor() > 250:
        player.goto(0, -280)
        car.increase_speed()
        scoreboard.next_level()

    for n_car in car.all_cars:
        if player.distance(n_car) < 20:
            game_is_on = False
            scoreboard.game_over()
            break

screen.exitonclick()
