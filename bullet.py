from turtle import Turtle


class Bullet(Turtle):
    def __init__(self, xcor, ycor):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=0.25)
        self.color('red')
        self.penup()
        self.goto(x=xcor, y=ycor + 10)
