from turtle import Turtle

from bullet import Bullet


class Alien(Turtle):
    """create the alien ship"""

    def __init__(self, shape='turtle', position=(0, 0),
                 color='white',
                 ship_size=1.5):
        super().__init__()
        self.penup()
        self.setheading(90)
        self.shape(shape)
        self.shapesize(stretch_wid=ship_size)
        self.goto(position)
        self.color(color)
        self.bullets = []

    def fire(self):
        """fire a new bullet"""
        bullet = Bullet(self.xcor(), self.ycor())
        self.bullets.append(bullet)
