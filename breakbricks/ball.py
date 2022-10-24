from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.num = 0
        self.moving_speed = 0.1

    def move(self):
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        self.goto(x, y)

    def bounce(self):
        self.y_move *= -1

    def collision(self):
        self.x_move *= -1
        self.moving_speed -= 0.01

    def reset(self):
        self.goto(0, 0)
        self.collision()
        self.moving_speed = 0.1
