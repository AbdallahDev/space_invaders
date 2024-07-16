import random
import time
import turtle

from scoreboard import ScoreBoard
from space_ship import SpaceShip

turtle.setup(width=600, height=600)
turtle.bgcolor('black')
turtle.tracer(n=0)
turtle.colormode(255)

SHIP_SPEED = 0.5
SLEEP_TIME = 0.001
enemy_ships = []


def enemy_ship():
    colors = [(233, 216, 166), (0, 95, 115), (10, 147, 150), (148, 210, 189), (238, 155, 0), (241, 250, 238), ]
    chance = random.randint(1, 40)
    if chance == 5 and len(enemy_ships) < 3:
        ship = turtle.Turtle(shape="turtle")
        ship.setheading(to_angle=270)
        print(random.choice(colors))
        ship.color(random.choice(colors))
        ship.penup()
        ship.goto(x=random.randint(-280, 280), y=300)
        enemy_ships.append(ship)


space_ship = SpaceShip()
bullets = space_ship.bullets

turtle.listen()
turtle.onkeypress(fun=space_ship.go_right, key="Right")
turtle.onkeypress(fun=space_ship.go_left, key="Left")
turtle.onkeypress(fun=space_ship.fire, key="space")

scoreboard = ScoreBoard()

game_on = True
game_time = 0
while game_on:
    enemy_ship()
    for bullet in bullets:
        bullet.goto(x=bullet.xcor(), y=bullet.ycor() + 10)
        for ship in enemy_ships:
            if bullet.distance(ship) < 10:
                scoreboard.update_score()

                bullet.reset()
                bullet.color("white")
                ship.reset()
                ship.penup()
                ship.goto(x=0, y=310)
                enemy_ships.remove(ship)

        if bullet.ycor() > 300:
            bullet.reset()
            bullet.penup()
            bullet.goto(x=0, y=-350)
            bullets.remove(bullet)
    for ship in enemy_ships:
        ship.goto(x=ship.xcor(), y=ship.ycor() - SHIP_SPEED)
        if ship.ycor() < -300:
            ship.reset()
            enemy_ships.remove(ship)

            game_on = False
            break

    turtle.update()
    time.sleep(SLEEP_TIME)
    game_time += 0.001
    print(len(bullets), len(enemy_ships))

scoreboard.game_over()

turtle.mainloop()
