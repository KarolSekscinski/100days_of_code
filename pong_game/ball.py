from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move_ball(self):
        future_x = self.xcor() + self.x_move
        future_y = self.ycor() + self.y_move
        self.goto(future_x, future_y)

    def bounce(self):
        self.y_move *= -1

    def hit_ball(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_pos(self):
        self.home()
        self.x_move *= -1
        self.move_speed = 0.1



