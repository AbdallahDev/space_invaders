from turtle import Turtle

from part import Part

SHAPE = 'square'
COLOR = 'white'


class Wall(Turtle):
    """Creates the protection wall from bricks"""

    def __init__(self, bricks_positions):
        super().__init__()
        self.hideturtle()
        self.bricks = []
        self.build_wall(bricks_positions)

    def build_wall(self, positions):
        coordinates = positions
        for cor in coordinates:
            brick = Part((cor[0], cor[1]))
            self.bricks.append(brick)

    def check_bricks_hit(
            self,
            bullet,
            # spaceship_bullets,
            # aliens_manager_obj,
            # aliens_bullets,
    ):
        for brick in self.bricks:
            if brick.check_hit(bullet):
                self.bricks.remove(brick)
                return True
        #     for bullet in spaceship_bullets:
        #         if brick.distance(bullet)<10:
        #             brick.destroy_part()
        #             self.bricks.remove(brick)
        #             bullet.destroy_bullet()
        #             spaceship_bullets.remove(bullet)
        #     if aliens_manager_obj.find_shooter(
        #             brick_obj=brick
        #     ):
        #         self.bricks.remove(brick)

    def hit_by_alien(self, aliens_bullets_list):
        pass

    def hit_by_spaceship(self):
        pass
