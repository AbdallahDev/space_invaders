from turtle import Turtle


class Part(Turtle):
    """Represent the defence wall brick
    or the spaceship part"""

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

    def check_hit(self, bullet):
        """check if the part took a hit
        by a bullet"""
        if self.distance(bullet) < 10:
            self.destroy_part()
            return True
