from turtle import Turtle
SCORE_POSITION = (-10, 300)
ALIGNMENT = "center"
FONTS = ("Arial", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("../../Desktop/data.txt") as f:
            self.high_score = int(f.read())

        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(SCORE_POSITION)
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()

    def update_score(self):
        self.clear()

        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONTS)

    def reset_game(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("../../Desktop/data.txt", mode="w") as f:
                f.write(str(self.high_score))
        self.score = 0
        self.update_score()



