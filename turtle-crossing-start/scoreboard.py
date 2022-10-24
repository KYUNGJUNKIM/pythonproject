from turtle import Turtle

ALIGN = "left"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-270, 270)
        self.level = 1
        self.update()

    def update(self):
        self.clear()
        self.write(f"Current Level: {self.level}", align=ALIGN, font=FONT)
        self.level += 1

    def gameover(self):
        self.clear()
        self.write("Game Over.", align=ALIGN, font=FONT)

