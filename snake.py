from turtle import Turtle, Screen

POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.seg = []
        self.create_snake()
        self.head = self.seg[0]

    def create_snake(self):
        for i in POSITION:
            self.add_segment(i)

    def add_segment(self, i):
        t = Turtle()
        t.penup()
        t.color("white")
        t.shape("square")
        t.goto(i)
        self.seg.append(t)

    def extend(self):
        self.add_segment(self.seg[-1].position())

    def move(self):
        for j in range(len(self.seg) - 1, 0, -1):
            new_x = self.seg[j - 1].xcor()
            new_y = self.seg[j - 1].ycor()
            self.seg[j].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)