from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=800, height=700)
user_bet = screen.textinput(title="Make a bet.", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple", "black"]
y_positions = [-150, -100, -50, 0, 50, 100, 150]
all_turtles = []
if user_bet:
    is_race_on = True

for turtle_index in range(0, 7):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.color(colors[turtle_index])
    tim.goto(x=-350, y=y_positions[turtle_index])
    all_turtles.append(tim)
print(all_turtles)
while is_race_on:
    for turtle in all_turtles:
        rand_distance = random.randint(0, 20)
        turtle.forward(rand_distance)
        turtle_index = all_turtles.index(turtle)
        if turtle.xcor() > 380:
            if colors[turtle_index] == user_bet:
                print(f"Your {colors[turtle_index]} turtle wins. Congrats!")

            else:
                print(f"The winner is {colors[turtle_index]} turtle. You lose.")
            is_race_on = False


screen.exitonclick()
