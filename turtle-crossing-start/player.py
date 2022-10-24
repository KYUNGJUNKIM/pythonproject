from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.seth(90)
        self.goto(STARTING_POSITION)

    def move_up(self):
        y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), y)

    def move_down(self):
        y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), y)

    def move_right(self):
        x = self.xcor() + MOVE_DISTANCE
        self.goto(x, self.ycor())

    def move_left(self):
        x = self.xcor() - MOVE_DISTANCE
        self.goto(x, self.ycor())

