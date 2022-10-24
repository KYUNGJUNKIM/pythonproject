from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
from scoreboard2 import ScoreBoard2
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

l_paddle = Paddle(-350, 0)
r_paddle = Paddle(350, 0)
ball = Ball()
scoreboard1 = ScoreBoard()
scoreboard2 = ScoreBoard2()

screen.listen()
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

game_on = True
while game_on:
    time.sleep(ball.moving_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -270:
        ball.bounce()
    if ball.distance(l_paddle) <= 50 and ball.xcor() <= -330:
        ball.collision()
        scoreboard1.get_score()
    if ball.distance(r_paddle) <= 50 and ball.xcor() >= 330:
        ball.collision()
        scoreboard2.get_score()

    if ball.xcor() > 360 and ball.distance(r_paddle) > 50:
        ball.reset()
        scoreboard2.lose_life()
    if ball.xcor() < -360 and ball.distance(r_paddle) > 50:
        ball.reset()
        scoreboard1.lose_life()

    if scoreboard1.life == 0:
        scoreboard1.gameover()
        scoreboard2.win()
        break
    elif scoreboard2.life == 0:
        scoreboard2.gameover()
        scoreboard1.win()
        break




screen.exitonclick()