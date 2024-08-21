from turtle import Turtle

from part import Part
from bullet import Bullet
from space_ship_part import SpaceShipPart


class SpaceShip(Turtle):
    def __init__(self, screen_height, screen_width):
        super().__init__()
        self.hideturtle()
        self.screen_limit = (screen_width / 2) - 50
        self.coordinates = []
        self.set_coordinates(
            start_y=-(screen_height / 2) + 50)
        self.parts = []
        self.build_spaceship()
        self.bullets = []

    def set_coordinates(self, start_y):
        """sets the spaceship parts coordinates"""
        xcor = 0
        ycor = start_y
        for i in range(9):
            if i == 1:
                xcor = self.coordinates[-1][0] - 20
                ycor = self.coordinates[-1][1] - 20
            elif i == 2 or i == 3:
                xcor = self.coordinates[-1][0] + 20
            self.coordinates.append((xcor, ycor))

    def build_spaceship(self):
        """builds the spaceship from parts"""
        for cord in self.coordinates:
            part = Part(coordinate=cord)
            self.parts.append(part)

    def fire(self):
        """creates a new bullet"""
        bullet = Bullet(
            self.parts[0].xcor(),
            self.parts[0].ycor())
        self.bullets.append(bullet)

    def move_bullets(self):
        """loops over the spaceship bullets
        to move them"""
        for bullet in self.bullets:
            bullet.move_bullet()

    def go_right(self):
        """moves the spaceship to the right"""
        if self.parts[0].xcor() < self.screen_limit:
            for part in self.parts:
                part.goto(
                    y=part.ycor(),
                    x=part.xcor() + 9)

    def go_left(self):
        """moves the spaceship to the left"""
        if (self.parts[0].xcor() >
                -self.screen_limit):
            for part in self.parts:
                part.goto(
                    y=part.ycor(),
                    x=part.xcor() - 9)

    # def loop_parts(self, bullet_obj):
    #     for part in self.parts:
    #         if part.distance(bullet_obj) < 10:
    #             return True
    #     return False
