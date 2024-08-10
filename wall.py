from turtle import Turtle

SHAPE = 'square'
COLOR = 'white'


class Wall(Turtle):
    """Creates the protection wall"""

    def __init__(self, xcor, ycor):
        super().__init__()
        self.shape(SHAPE)
        self.color(COLOR)
        self.penup()
        self.goto(x=xcor, y=ycor)
        self.shapesize(3)
        self.hits = 0
