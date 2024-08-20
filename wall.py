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

    def check_bricks_hit(self, bullets_list):
        for brick in self.bricks:
            for bullet in bullets_list:
                if brick.take_hit(bullet_obj=bullet):
                    self.bricks.remove(brick)
                    bullet.remove_bullet()
                    bullets_list.remove(bullet)
