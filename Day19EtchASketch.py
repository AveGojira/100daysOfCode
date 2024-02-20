from turtle import Turtle, Screen

etcher = Turtle()
screen = Screen()


def move_forwards():
    etcher.forward(10)


def move_backwards():
    etcher.backward(10)


def turn_left():
    new_heading = etcher.heading() + 10
    etcher.setheading(new_heading)


def turn_right():
    new_heading = etcher.heading() - 10
    etcher.setheading(new_heading)


def clear():
    etcher.clear()
    etcher.penup()
    etcher.home()
    etcher.pendown()


screen.listen()
screen.onkey(move_forwards, "Up")
screen.onkey(move_backwards, "Down")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
screen.onkey(clear, "c")

screen.exitonclick()
