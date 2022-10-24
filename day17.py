from turtle import Turtle, Screen
import random

my_turtle = Turtle()
my_turtle.pensize(10)
state = True
angle = [0, 90, 180, 270]
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

while state:
    my_turtle.seth(random.choice(angle))
    my_turtle.color(random.choice(colours))
    my_turtle.forward(100)


screen = Screen()
screen.exitonclick()

