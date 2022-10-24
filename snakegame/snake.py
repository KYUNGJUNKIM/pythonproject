from turtle import Turtle

STARTING_POINTS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):
        self.snakes = []
        self.make()
        self.head = self.snakes[0]

    def make(self):
        for point in STARTING_POINTS:
            self.add_snake(point)

    def add_snake(self, position):
        snake = Turtle("square")
        snake.color("white")
        snake.up()
        snake.goto(position)
        self.snakes.append(snake)

    def extend(self):
        self.add_snake(self.snakes[-1].pos())

    def move(self):
        for num in range(len(self.snakes) - 1, 0, -1):
            x = self.snakes[num - 1].xcor()
            y = self.snakes[num - 1].ycor()
            self.snakes[num].goto(x, y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def go_home(self):
        for snake in self.snakes:
            snake.hideturtle()
        self.snakes.clear()
        self.make()
        self.head = self.snakes[0]


