from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 20
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.shape("turtle")
        self.start_game()

    def start_game(self):
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def move_turtle(self):
        current_y = self.ycor()
        self.goto(self.xcor(), current_y + MOVE_DISTANCE)

    def success(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False



