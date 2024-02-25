from turtle import Turtle


class CourtMarks(Turtle):

    def __init__(self):
        super().__init__()
        self.sety(300)
        self.pensize(5)
        self.right(90)
        self.color("white")

        for _ in range(30):
            self.forward(10)
            self.penup()
            self.forward(20)
            self.pendown()
