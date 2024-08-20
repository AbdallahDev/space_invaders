from turtle import Turtle

from part import Part

SHAPE = 'square'
COLOR = 'white'


class Wall(Turtle):
    """Creates the protection wall from bricks"""

    def __init__(self, bricks_positions):
        super().__init__()
        self.hideturtle()
        self.parts = []
        self.build_wall(bricks_positions)

    def build_wall(self, positions):
        coordinates = positions
        for cor in coordinates:
            brick = Part((cor[0], cor[1]))
            self.parts.append(brick)

    def check_bricks_hit(self, bullets_list):
        for part in self.parts:
            for bullet in bullets_list:
                if part.take_hit(bullet_obj=bullet):
                    self.parts.remove(part)
                    bullet.remove_bullet()
                    bullets_list.remove(bullet)
