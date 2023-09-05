from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.cars_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            car = Turtle("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(random.choice(COLORS))
            car.penup()
            car_y = random.randint(-250, 250)
            car.goto(300, car_y)
            self.all_cars.append(car)

    def move_cars(self):

        for car in self.all_cars:
            car.backward(self.cars_speed)
            if car.xcor() < -350:
                self.all_cars.remove(car)

    def increase_speed(self):
        self.cars_speed += MOVE_INCREMENT









