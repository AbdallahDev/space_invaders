import random
import time
import turtle

from aliens_manager import AliensManager
from defence_manager import DefenceManager
from scoreboard import ScoreBoard
from space_ship import SpaceShip

# this represents the screen height,
# the width will be the double of it
SCREEN_HEIGHT = 600
SCREEN_WIDTH = SCREEN_HEIGHT * 2
BG_COLOR = 'black'
SCREEN_START_X = 10
# SHIP_SPEED = 0.5
SLEEP_TIME = 0.001

turtle.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT,
             startx=SCREEN_START_X)
turtle.bgcolor(BG_COLOR)
turtle.tracer(n=0)
turtle.colormode(255)
turtle.listen()

space_ship = SpaceShip(
    screen_height=SCREEN_HEIGHT,
    screen_width=SCREEN_WIDTH
)
turtle.onkeypress(fun=space_ship.go_right, key="Right")
turtle.onkeypress(fun=space_ship.go_left, key="Left")
turtle.onkeypress(fun=space_ship.fire, key="space")

aliens_manager = AliensManager(
    screen_height=SCREEN_HEIGHT,
    screen_width=SCREEN_WIDTH,
    ships_count=50)
# aliens = aliens_manager.ships

scoreboard = ScoreBoard(
    screen_width=SCREEN_WIDTH,
    screen_height=SCREEN_HEIGHT)

defence_manager = DefenceManager()

game_on = True
game_time = 0
bullet_hit_something = False

while game_on:
    space_ship.move_bullets()
    aliens_manager.attack()
    defence_manager.check_walls_hit(
        spaceship_bullets=space_ship.bullets,
        aliens_manager_obj=aliens_manager,
        # aliens_bullets=aliens_manager.ships_bullets(),
    )

    # bullets = space_ship.bullets+aliens_manager.ships_bullets()
    # bullets = []
    # bullets.extend(space_ship.bullets)
    # bullets.extend(aliens_manager.ships_bullets())
    # for bullet in bullets:
    #     # print(bullet.color(), len(bullets))
    #     pass
    # if (len(space_ship.bullets) > 0
    #         or len(aliens_manager.ships_bullets()) > 0):
    #     bullets.extend(space_ship.bullets)
    #     bullets.extend(aliens_manager.ships_bullets())
    # if len(bullets) > 0:
    #     for bullet in bullets:
    #         print(bullet.color())
    #     defence_manager.check_walls_hit(bullets_list=bullets)

    # game_on = (
    #     aliens_manager.loop_over_ships(
    #         space_ship_obj=space_ship,
    #         defence_manager_obj=defence_manager,
    #     ))

    # for bullet in space_ship_bullets:
    #     bullet.goto(x=bullet.xcor(), y=bullet.ycor() + 10)
    #     for alien in aliens:
    #         # I'll loop over the ships to check if any of them has been
    #         # hit by the bullet
    #         if bullet.distance(alien) < 10:
    #             scoreboard.update_score()
    #
    #             # here if the bullet hits the alien ship it will disappear
    #             space_ship_bullets.remove(bullet)
    #             bullet.remove_bullet()
    #
    #             alien.reset()
    #             alien.penup()
    #             alien.goto(x=0, y=310)
    #             aliens.remove(alien)
    #
    #     for wall in defence_manager.walls:
    #         # I'll loop over the walls to check if any one of the has been hit by
    #         # any bullet.
    #         # wall.take_hits(bullet)
    #         for brick in wall.bricks:
    #             if brick.distance(bullet) < 10:
    #                 space_ship_bullets.remove(bullet)
    #                 bullet.remove_bullet()
    #
    #                 brick.reset()
    #                 brick.hideturtle()
    #                 brick.penup()
    #                 wall.bricks.remove(brick)
    #
    #     # here if the bullet exceed the screen limits it will disappear
    #     if bullet.ycor() > SCREEN_HEIGHT / 2:
    #         space_ship_bullets.remove(bullet)
    #         bullet.remove_bullet()

    turtle.update()
    time.sleep(SLEEP_TIME)
    game_time += 0.001

scoreboard.game_over()

turtle.mainloop()
