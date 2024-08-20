from wall import Wall


class DefenceManager:
    """Takes care of the defence by making walls"""

    def __init__(self):
        self.walls = []
        self.making_defence()

    def making_defence(self):
        positions = [
            [
                (-220, -150), (-200, -150), (-180, -150),
                (-220, -170), (-200, -170), (-180, -170),
            ],
            [
                (-20, -150), (0, -150), (20, -150),
                (-20, -170), (0, -170), (20, -170),
            ],
            [
                (180, -150), (200, -150), (220, -150),
                (180, -170), (200, -170), (220, -170),
            ],
        ]
        for position in positions:
            wall = Wall(bricks_positions=position)
            self.walls.append(wall)

    def check_walls_hit(self, bullets_list):
        for wall in self.walls:
            wall.check_bricks_hit(bullets_list=bullets_list)
