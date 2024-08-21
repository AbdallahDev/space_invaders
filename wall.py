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
            spaceship_bullets,
            aliens_manager_obj,
            # aliens_bullets,
    ):
        for brick in self.bricks:
            for bullet in spaceship_bullets:
                # pass
                if brick.distance(bullet)<10:
                        # brick.take_hit(
                        # bullet_obj=bullet):
                    brick.take_hit()
                    self.bricks.remove(brick)
                    bullet.destroy_bullet()
                    spaceship_bullets.remove(bullet)
            if aliens_manager_obj.find_shooter(
                    brick_obj=brick
            ):
                self.bricks.remove(brick)
            # for bullet in aliens_bullets:
            #     if brick.take_hit(
            #             bullet_obj=bullet):
            #         self.parts.remove(brick)
            #         bullet.destroy_bullet()

    def hit_by_alien(self, aliens_bullets_list):
        pass

    def hit_by_spaceship(self):
        pass
