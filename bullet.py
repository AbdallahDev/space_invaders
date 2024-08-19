import random
from turtle import Turtle


class Bullet(Turtle):
    def __init__(self, xcor, ycor):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=0.25)
        self.color('red')
        self.penup()
        self.speed(1)
        self.goto(x=xcor, y=ycor + 10)

    def remove_bullet(self):
        # deals with the bullet removing.
        self.reset()
        self.hideturtle()
        self.penup()

    def move_bullet(self):
        random_int = random.randint(0, 50)
        if random_int > 45:
            self.goto(x=self.xcor(), y=self.ycor() - 10)
