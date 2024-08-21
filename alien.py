import random
from turtle import Turtle

from bullet import Bullet


class Alien(Turtle):
    """create the alien ship"""

    def __init__(self,
                 shape='turtle',
                 position=(0, 0),
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
        """creates a new bullet"""
        self.bullets.append(
            Bullet(
                self.xcor(), self.ycor()))

    def move_bullets(self):
        """loops over the alien bullets
        to move them"""
        for bullet in self.bullets:
            bullet.move_bullet(
                direction=-1,
                speed=2)

    def find_shooting_bullet(self,
                             brick_obj
                             ):
        for bullet in self.bullets:
            if bullet.distance(brick_obj) < 10:
                bullet.destroy_bullet()
                self.bullets.remove(bullet)
                return True

    def remove_bullet(self, bullet):
        self.bullets.remove(bullet)

    def check_hit(self, bullet):
        """check for a hit from the spaceship"""
        if self.distance(bullet) < 10:
            self.destroy_ship()
            return True

        # for bullet in bullets:
        #     if self.distance(bullet) < 10:
        #         self.destroy_ship()
        #         bullet.destroy_bullet()
        #         bullets.remove(bullet)

    def destroy_ship(self):
        """destroys the ship after it takes a hit
        by a bullet"""
        self.reset()
        self.hideturtle()
        self.penup()
