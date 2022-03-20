import random
from turtle import Turtle
FOOD_POSITION = [-280, 280]


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('circle')
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('blue')
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        rand_x = random.randint(FOOD_POSITION[0], FOOD_POSITION[1])
        rand_y = random.randint(FOOD_POSITION[0], FOOD_POSITION[1])
        self.goto(rand_x, rand_y)

