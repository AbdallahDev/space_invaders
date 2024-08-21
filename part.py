from turtle import Turtle


class Part(Turtle):
    """Represent the defence wall brick"""

    def __init__(self, coordinate):
        super().__init__()
        self.penup()
        self.shapesize(1)
        self.shape("square")
        self.color('white')
        self.goto(
            x=coordinate[0],
            y=coordinate[1])

    def destroy_part(self):
        self.reset()
        self.hideturtle()
        self.penup()
