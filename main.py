import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()

car_manager = CarManager()

screen.listen()
screen.onkey(player.move, 'Up')

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False

    if player.win():
        scoreboard.score += 1
        scoreboard.print_scoreboard()
        car_manager.level_up()
        player.return_to_start()

screen.exitonclick()
