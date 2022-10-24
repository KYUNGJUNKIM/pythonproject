from turtle import Turtle, Screen
import random

red = Turtle()
orange= Turtle()
yellow = Turtle()
green = Turtle()
blue = Turtle()
indigo = Turtle()
purple = Turtle()

turtle_list = [red, orange, yellow, green, blue, indigo, purple]

red.color("red")
red.shape("turtle")
orange.color("orange")
orange.shape("turtle")
yellow.color("yellow")
yellow.shape("turtle")
green.color("green")
green.shape("turtle")
blue.color("blue")
blue.shape("turtle")
indigo.color("indigo")
indigo.shape("turtle")
purple.color("purple")
purple.shape("turtle")

guess = input("Which color of turtle would like to win?: ")

i = 0
for turtle in turtle_list:
    turtle.xpos(-350)
    turtle.ypos(-220+(i*80))
    i += 1

for turtle in turtle_list:
    if turtle.xpos(350):
        print(f"The winner is: {turtle}")
        if turtle == guess:
            print("Guess right")
        else:
            print("You've got the wrong answer.")
        quit()

    turtle.forward(random.randint(10, 50))



screen = Screen()



screen.exitonclick()


