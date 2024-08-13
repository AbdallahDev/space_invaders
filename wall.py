from turtle import Turtle

from brick import Brick

SHAPE = 'square'
COLOR = 'white'


class Wall(Turtle):
    """Creates the protection wall from bricks"""

    def __init__(self, bricks_positions):
        super().__init__()
        self.hideturtle()
        self.bricks = []
        self.make_wall(bricks_positions)

    def make_wall(self, positions):
        coordinates = positions
        for cor in coordinates:
            brick = Brick((cor[0], cor[1]))
            self.bricks.append(brick)

    def take_hits(self, bullet):
        for brick in self.bricks:
            pass
