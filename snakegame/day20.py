from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    snake.move()
    if snake.head.distance(food) < 15:
        scoreboard.get_score()
        snake.extend()
        food.goto(random.randint(-270, 270), random.randint(-270, 270))

    if snake.head.xcor() < -290 or snake.head.xcor() > 290 or snake.head.ycor() < -290 or snake.head.ycor() > 290:
        scoreboard.reset()
        snake.go_home()

    for segment in snake.snakes:
        if segment == snake.head:
            pass
        elif segment.distance(snake.head) < 10:
            scoreboard.reset()
            snake.go_home()

    with open("record.txt", "r") as record:
        string = record.readline()
        scoreboard.highest = int(string)

# ANOTHER SOLUTION FOR COLLISION
# for snake in snake.snakes:
#     if snake == snake.head:
#         pass
#     elif snake.head.distance(snake) < 10:
#         scoreboard.gameover()
#         game_on = False



screen.exitonclick()
