from turtle import *
POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.head.shape("snakehead_small.gif")
        self.head.shapesize(stretch_wid=0.5, stretch_len=0.5)

    def create_snake(self):
        for i in POSITIONS:
            self.add_segments(i)

    def add_segments(self, i):
        timmy = Turtle()
        timmy.shape("square")
        timmy.speed("fastest")
        timmy.color("#A3CE30")
        timmy.penup()
        timmy.goto(i)
        self.segments.append(timmy)

    def extend_snake(self):
        self.add_segments(self.segments[-1].position())

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
            self.head.shape("head_up.gif")

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
            self.head.shape("head_down.gif")

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
            self.head.shape("head_left.gif")

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
            self.head.shape("head_right.gif")
