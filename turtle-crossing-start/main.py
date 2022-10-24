import time
from turtle import Screen
from player import Player
from scoreboard import Scoreboard
from car_manager import CarManager

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Crossing GAME")

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_down, "Down")
screen.onkey(player.move_left, "Left")
screen.onkey(player.move_right, "Right")

cnt = 0
game_is_on = True
while game_is_on:
    time.sleep(0.3)
    screen.update()
    cnt += 1

    if cnt % 3 == 0:
        car_manager.create()
        car_manager.move()

    for car in car_manager.cars:
        if car.distance(player) < 25:
            scoreboard.gameover()
            game_is_on = False

    if player.ycor() >= 280:
        scoreboard.update()
        player.goto(0, -280)
        car_manager.level_up()

screen.exitonclick()


