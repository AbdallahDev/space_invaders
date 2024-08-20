import random
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
        self.bullets.append(Bullet(self.xcor(), self.ycor()))

    def loop_over_bullets(self, space_ship_obj,
                          defence_manager_obj):
        for bullet in self.bullets:
            if random.randint(0, 50) > 45:
                bullet.move_bullet(direction=-1)
            if space_ship_obj.loop_parts(bullet_obj=bullet):
                bullet.remove_bullet()
                self.bullets.remove(bullet)
                return False
            # elif defence_manager_obj.check_walls_hit():
            #     self.bullets.remove(bullet)
            #     bullet.remove_bullet()
        return True

    def remove_bullet(self, bullet):
        self.bullets.remove(bullet)
