from turtle import Turtle

from brick import Brick
from bullet import Bullet
from space_ship_part import SpaceShipPart

PARTS_LENGTH = [3, 1.5, 0.25]


class SpaceShip(Turtle):
    def __init__(self, screen_height, screen_width):
        super().__init__()
        self.hideturtle()
        self.screen_limit = (screen_width / 2) - 50
        # self.screen_width = screen_width
        # self.initial_ycor = -(screen_height / 2) + 20
        self.coordinates = []
        self.set_coordinates(start_y=-(screen_height / 2) + 50)
        self.parts = []
        self.build_parts()
        self.bullets = []

    def set_coordinates(self, start_y):
        xcor = 0
        ycor = start_y
        for i in range(9):
            if i == 1:
                xcor = self.coordinates[-1][0] - 20
                ycor = self.coordinates[-1][1] - 20
            elif i == 2 or i == 3:
                xcor = self.coordinates[-1][0] + 20
            self.coordinates.append((xcor, ycor))

    def build_parts(self):
        """build the spaceship parts"""
        for cord in self.coordinates:
            part = Brick(coordinate=cord)
            self.parts.append(part)

    def fire(self):
        """fire a new bullet"""
        bullet = Bullet(self.parts[0].xcor(), self.parts[0].ycor())
        self.bullets.append(bullet)
        # self.move_bullets()

    def go_right(self):
        if self.parts[0].xcor() < self.screen_limit:
            for part in self.parts:
                part.goto(y=part.ycor(), x=part.xcor() + 9)

    def go_left(self):
        if self.parts[0].xcor() > -self.screen_limit:
            for part in self.parts:
                part.goto(y=part.ycor(), x=part.xcor() - 9)

    def loop_parts(self, bullet_obj):
        for part in self.parts:
            if part.distance(bullet_obj) < 10:
                return True
        return False

    def move_bullets(self):
        for bullet in self.bullets:
            bullet.move_bullet()
