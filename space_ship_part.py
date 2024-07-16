from turtle import Turtle


class SpaceShipPart(Turtle):
    def __init__(self, length, ycor):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=0.5, stretch_len=length)
        self.color('white')
        self.penup()
        self.goto(x=0, y=ycor)
