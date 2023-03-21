import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard, RoadLines
from random import randint


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
roadlines = RoadLines()

def register_key():
    screen.onkey(key="Up", fun=player.move)

screen.listen()
screen.ontimer(register_key, 5000)



game_is_on = True
roadlines.make_roads()
scoreboard.first_level()
while game_is_on:
    if player.ycor() > 220:
        scoreboard.next_level()
        player.respawn()
        # car_manager.clear_cars() (this is an entire function I made for no reason because im a dumb a##)
        screen.ontimer(register_key, 5000)
    if randint(1, 2) == 1:
        car_manager.spawn_cars()
    car_manager.move_cars()
    for cars in car_manager.all_cars:
        if player.distance(cars) < 20:
            car_manager.clear_cars()
            scoreboard.game_over()
            player.die()
            game_is_on = False

    time.sleep(0.1)
    screen.update()
screen.exitonclick()
