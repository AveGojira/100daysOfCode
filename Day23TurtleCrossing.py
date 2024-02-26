import time
from turtle import Screen
from Day23TurtleCrossing_Player import Player
from Day23TurtleCrossing_Cars import CarManager
from Day23TurtleCrossing_Scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.go_up, "Up")


turtles_Crossing = True
while turtles_Crossing:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

# squish detection, gets worse as levels progress unfortunately
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            turtles_Crossing = False
            scoreboard.game_over()

# determines if the player got the finish line, to start a new level and speed up cars
    if player.finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()
