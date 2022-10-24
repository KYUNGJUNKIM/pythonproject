from turtle import Turtle, Screen
FONT = ("Arial", 14, "normal")
SCREEN = Screen()

class ScoreBoard2(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        SCREEN.tracer(0)
        self.goto(180, 260)
        self.life = 3
        self.update()

    def update(self):
        SCREEN.update()
        self.write(f"P2 Current Score: {self.score}, \n Current Life: {self.life}", align="center", font=FONT)

    def gameover(self):
        self.clear()
        self.write(f"Sorry P2, Game Over. \n Final Score: {self.score}", align="center", font=FONT)

    def win(self):
        self.clear()
        self.write(f"Congratulations. P2 win. \n Final Score: {self.score}", align="center", font=FONT)

    def get_score(self):
        self.score += 1
        self.clear()
        self.update()

    def lose_life(self):
        self.life -= 1
        self.clear()
        self.update()

