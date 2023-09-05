from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time

screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)


player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_turtle, "Up")

collision = 20
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Detect collisions with cars
    for car in car_manager.all_cars:
        if player.distance(car) < collision:
            scoreboard.game_over()
            game_is_on = False

    # Detect when the player has reached the other side
        if player.success():
            scoreboard.increase_level()
            car_manager.increase_speed()
            scoreboard.update_scoreboard()
            player.start_game()
            collision += 1



screen.exitonclick()
