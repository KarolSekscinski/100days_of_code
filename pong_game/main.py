from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
screen = Screen()
screen.tracer(0)
screen.setup(width=1000, height=800)
screen.bgcolor("black")
screen.title("My Pong Game")

r_paddle = Paddle((450, 0))
l_paddle = Paddle((-450, 0))

ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball()

    # Detect collisions with wall
    if ball.ycor() > 380 or ball.ycor() < -380:
        ball.bounce()
    # Detect collisions with paddle
    if (ball.xcor() > 430 or ball.xcor() < -430) and (r_paddle.distance(ball) < 50 or l_paddle.distance(ball) < 50):
        ball.hit_ball()

    # Detect paddle misses
    if ball.xcor() > 480:
        ball.reset_pos()
        scoreboard.l_user_scores()

    if ball.xcor() < -480:
        ball.reset_pos()
        scoreboard.r_user_scores()







screen.exitonclick()
