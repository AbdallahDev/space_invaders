import random

from alien import Alien

ATTACK_RANGE_FROM = 0
ATTACK_RANGE_TO = 6000
ATTACK_RANGE_CHANCE = 0


class AliensManager:
    """Manages the alien ships"""

    def __init__(self, screen_width, screen_height,
                 ships_count=50):
        self.count = ships_count
        self.ships = []
        self.gather_ships(
            start_x=-(screen_width / 2) + 380,
            start_y=(screen_height / 2) - 150)

    def gather_ships(self, start_x, start_y):
        """creating the ships group"""
        number_of_rows = int(self.count / 10)
        number_of_ships_per_row = 10
        x_space = 50
        y_space = 50
        x = start_x
        y = start_y
        for row in range(number_of_rows):
            for _ in range(number_of_ships_per_row):
                alien = Alien(position=(x, y))
                self.ships.append(alien)
                x += x_space
            x = start_x
            y -= y_space

    def ship_attack(self):
        """chooses a random ship to shoot"""
        if (random.randint(ATTACK_RANGE_FROM,
                           ATTACK_RANGE_TO) ==
                ATTACK_RANGE_CHANCE):
            random.choice(self.ships).fire()

    def find_shooter(self, brick_obj):
        for ship in self.ships:
            # number_of_bullets = len(ship.bullets)
            # if number_of_bullets > 0:
            #     print(
            #         self.ships.index(ship),
            #         number_of_bullets)
            if ship.find_shooting_bullet(
                    brick_obj=brick_obj
            ):
                brick_obj.destroy_part()
                return True
            # self.ship_attack()
            # ship.move_bullets()

    def attack(self):
        """loops over the ships to move
        their bullets"""
        for ship in self.ships:
            self.ship_attack()
            ship.move_bullets()

    def ships_bullets(self):
        bullets = []
        for ship in self.ships:
            if len(ship.bullets) > 0:
                for bullet in ship.bullets:
                    print(bullet.color())
                bullets.append(ship.bullets)
            return bullets

    def check_ships_hit(self, spaceship_bullets):
        """checks if there is any ship took a hit"""
        for ship in self.ships:
            if ship.check_hit(spaceship_bullets):
                self.ships.remove(ship)
