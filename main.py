import random
import time
import turtle

from aliens_manager import AliensManager
from defence_manager import DefenceManager
from scoreboard import ScoreBoard
from space_ship import SpaceShip
from wall import Wall

# this represents the screen height, the width will be the double of it
SCREEN_HEIGHT = 600
SCREEN_WIDTH = SCREEN_HEIGHT * 2
BG_COLOR = 'black'
SCREEN_START_X = 10
SHIP_SPEED = 0.5
SLEEP_TIME = 0.001

turtle.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT, startx=SCREEN_START_X)
turtle.bgcolor(BG_COLOR)
turtle.tracer(n=0)
turtle.colormode(255)


def remove_bullet(bullet_obj):
    # deals with the bullet removing.
    bullet_obj.reset()
    bullet_obj.hideturtle()
    bullet_obj.penup()


aliens_manager = AliensManager(screen_height=SCREEN_HEIGHT, screen_width=SCREEN_WIDTH, ships_count=50)
enemy_ships = aliens_manager.ships
space_ship = SpaceShip(screen_height=SCREEN_HEIGHT, screen_width=SCREEN_WIDTH)
bullets = space_ship.bullets

turtle.listen()
turtle.onkeypress(fun=space_ship.go_right, key="Right")
turtle.onkeypress(fun=space_ship.go_left, key="Left")
turtle.onkeypress(fun=space_ship.fire, key="space")

scoreboard = ScoreBoard(screen_width=SCREEN_WIDTH, screen_height=SCREEN_HEIGHT)
defence_manager = DefenceManager(screen_width=SCREEN_WIDTH, screen_height=SCREEN_HEIGHT)

game_on = True
game_time = 0
while game_on:
    for bullet in bullets:
        bullet.goto(x=bullet.xcor(), y=bullet.ycor() + 10)
        for ship in enemy_ships:
            if bullet.distance(ship) < 10:
                scoreboard.update_score()

                # here if the bullet hits the alien ship it will disappear
                bullets.remove(bullet)
                remove_bullet(bullet)

                ship.reset()
                ship.penup()
                ship.goto(x=0, y=310)
                enemy_ships.remove(ship)

        # here if the bullet exceed the screen limits it will disappear
        if bullet.ycor() > SCREEN_HEIGHT / 2:
            bullets.remove(bullet)
            remove_bullet(bullet)

    turtle.update()
    time.sleep(SLEEP_TIME)
    game_time += 0.001

scoreboard.game_over()

turtle.mainloop()
