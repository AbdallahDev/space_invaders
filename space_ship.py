from turtle import Turtle

from part import Part
from bullet import Bullet


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

    def attack(self, defence_manager_obj, aliens_obj):
        """it will check if the bullets hit any object
        like the wall or the aliens"""
        for bullet in self.bullets:
            if defence_manager_obj.check_walls_hit(bullet):
                self.bullets.remove(bullet)
                bullet.destroy_bullet()
            if aliens_obj.check_ships_hit(bullet):
                bullet.destroy_bullet()
                self.bullets.remove(bullet)

    def check_parts_hit(self, bullet_obj):
        for part in self.parts:
            if part.check_hit(bullet_obj):
                self.parts.remove(part)
                return True

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
