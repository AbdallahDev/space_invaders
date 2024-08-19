import random
from turtle import Turtle

from bullet import Bullet
from space_ship import SpaceShip


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
        # bullet = Bullet(self.xcor(), self.ycor())
        self.bullets.append(Bullet(self.xcor(), self.ycor()))

    def loop_over_bullets(self, space_ship_obj):
        for bullet in self.bullets:
            bullet.move_bullet()
            value = space_ship_obj.loop_parts(bullet_obj=bullet)
            if value:
                bullet.remove_bullet()
                self.bullets.remove(bullet)
                return False
        return True

    # def move_bullets(self):
    #     for bullet in self.bullets:
    #         if random.randint(0, 50) > 45:
    #             bullet.move()

    def remove_bullet(self, bullet):
        self.bullets.remove(bullet)
