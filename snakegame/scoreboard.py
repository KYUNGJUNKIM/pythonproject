from turtle import Turtle
from snake import Snake

ALIGN = "center"
FONT = ("Arial", 16, "normal")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("record.txt", "r") as record:
            self.highest = int(record.read())
        self.color("white")
        self.up()
        self.hideturtle()
        self.sety(260)
        self.update()


    def update(self):
        self.clear()
        self.write(f"Current Score: {self.score} \n Highest Score: {self.highest}", align=ALIGN, font=FONT)

    def reset(self):
        if self.score > self.highest:
            self.highest = self.score
            with open("record.txt", "w") as record:
                record.write(str(self.highest))
        self.score = 0
        self.update()

    def get_score(self):
        self.score += 1
        self.update()


