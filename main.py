import random
from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

s = Snake()
food = Food()
score = Scoreboard()

scr = Screen()
scr.setup(width=600, height=600)
scr.bgcolor("black")
scr.title("Game")
scr.tracer(0)
scr.listen()
scr.onkey(s.up, "Up")
scr.onkey(s.down, "Down")
scr.onkey(s.left, "Left")
scr.onkey(s.right, "Right")

isOn = True
while isOn:
    # collision with wall
    if s.head.xcor() <= -280 or s.head.xcor() >= 280 or s.head.ycor() <= -280 or s.head.ycor() >= 280:
        isOn = False
        score.game_over()

    # collision with tail
    for j in s.seg[1:]:
        if s.head.distance(j) < 10:
            isOn = False
            score.game_over()

    scr.update()
    time.sleep(0.1)
    s.move()
    if s.head.distance(food) < 15:
        score.increase_score()
        food.refresh()
        s.extend()
scr.exitonclick()

scr.exitonclick()
#Created By Radhakrishan
