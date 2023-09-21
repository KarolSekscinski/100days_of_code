from turtle import Turtle, Screen, colormode
import random
list_of_colours = [(199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (222, 224, 227), (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151), (141, 171, 155), (179, 201, 186), (172, 153, 159), (212, 183, 177), (176, 198, 203), (150, 115, 120), (202, 185, 190), (40, 72, 82), (46, 73, 62), (47, 66, 82)]

colormode(255)
tim = Turtle()
tim.up()
tim.hideturtle()
tim.speed("fastest")
tim.setpos(-200, -200)

for _ in range(10):
    for _ in range(10):
        color = random.choice(list_of_colours)
        tim.color((color[0], color[1], color[2]))
        tim.dot(20)
        tim.forward(50)
    tim.goto(-200, tim.ycor() + 50)

screen = Screen()
screen.exitonclick()
