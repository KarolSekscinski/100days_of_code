from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.print_scoreboard()

    def print_scoreboard(self):
        self.clear()
        self.goto(-100, 250)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 250)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def l_user_scores(self):
        self.l_score += 1
        self.print_scoreboard()

    def r_user_scores(self):
        self.r_score += 1
        self.print_scoreboard()


