from turtle import Turtle


class Brick(Turtle):
    """Represent the defence wall brick"""

    def __init__(self, coordinate):
        super().__init__()
        self.penup()
        self.shapesize(1)
        self.shape("square")
        self.color('white')
        # print(type(coordinate))
        self.goto(x=coordinate[0], y=coordinate[1])
