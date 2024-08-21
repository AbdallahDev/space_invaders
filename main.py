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
BG_COLOR = 'Black'
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
    space_ship.attack(aliens_manager, defence_manager)
    aliens_manager.attack()
    # defence_manager.check_walls_hit(
    #     spaceship_bullets=space_ship.bullets,
    #     aliens_manager_obj=aliens_manager,
    # )
    # aliens_manager.check_ships_hit(
    #     space_ship.bullets)

    turtle.update()
    time.sleep(SLEEP_TIME)
    game_time += 0.001

scoreboard.game_over()

turtle.mainloop()
