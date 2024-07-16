from turtle import Turtle

from bullet import Bullet
from space_ship_part import SpaceShipPart

PARTS_LENGTH = [3, 1.5, 0.25]


class SpaceShip(Turtle):
    def __init__(self):
        super().__init__()
        self.parts = []
        self.build_parts()
        self.bullets = []

    def build_parts(self):
        """build the spaceship parts"""
        ycor = -280
        for i in range(3):
            part = SpaceShipPart(length=PARTS_LENGTH[i], ycor=ycor)
            self.parts.append(part)
            ycor += 10

    def fire(self):
        """fire a new bullet"""
        bullet = Bullet(self.parts[0].xcor(), self.parts[0].ycor())
        self.bullets.append(bullet)

    def go_right(self):
        for part in self.parts:
            part.goto(y=part.ycor(), x=part.xcor() + 10)

    def go_left(self):
        for part in self.parts:
            part.goto(y=part.ycor(), x=part.xcor() - 10)

    # def move_bullets(self):
    #     """move the bullets"""
    #     for ship in enemy_ships:
    #         if bullet.distance(ship) < 10:
    #             score += 1
    #             score_board.clear()
    #             score_board.write(arg=f"Score: {score}")
    #
    #             bullet.reset()
    #             bullet.color("black")
    #             ship.reset()
    #             ship.penup()
    #             ship.goto(x=0, y=310)
    #             enemy_ships.remove(ship)
