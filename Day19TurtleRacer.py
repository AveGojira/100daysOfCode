from turtle import Turtle, Screen
import random

race_active = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet!", prompt="Which color turtle will win the race?: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    racer = Turtle(shape="turtle")
    racer.penup()
    racer.color(colors[turtle_index])
    racer.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(racer)

if user_bet:
    race_active = True

while race_active:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            race_active = False
            winning_racer = turtle.pencolor()
            if winning_racer == user_bet:
                print(f"Congratulations! Your {winning_racer} turtle won the race!")
            else:
                print(f"Sorry, {winning_racer} has won the race.")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()
