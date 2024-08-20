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

    def take_hit(self, bullet_obj):
        if self.distance(bullet_obj) < 10:
            self.remove_brick()
            return True

    def remove_brick(self):
        self.reset()
        self.hideturtle()
        self.penup()
