from turtle import Screen
import time

from Day22Pong_Ball import Ball
from Day22Pong_Paddle import Paddle
from Day22Pong_Scoreboard import Scoreboard
from Day22Pong_Courtmarking import CourtMarks

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()
court_marks = CourtMarks()

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

pong_on = True
while pong_on:
    time.sleep(0.01)
    screen.update()
    ball.move()

    # detects collision with top and bottom walls in order to bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # collision detection for paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()

    # detect when right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # detect when left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
