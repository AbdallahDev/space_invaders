from alien import Alien


class AliensManager:
    """Manages the alien ships"""

    def __init__(self, screen_width, screen_height, ships_count=50):
        self.count = ships_count
        self.ships = []
        self.gather_ships(start_x=-(screen_width / 2) + 380, start_y=(screen_height / 2) - 150)

    def gather_ships(self, start_x, start_y):
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
