from wall import Wall


class DefenceManager:
    """Takes care of the defence by making walls"""

    def __init__(self, screen_width, screen_height):
        self.walls = []
        self.making_defence(3, -(screen_width / 2) + 410, (screen_height / 2) - 450)

    def making_defence(self, count, startx, starty):
        for index in range(count):
            wall = Wall(xcor=startx, ycor=starty)
            self.walls.append(wall)
            startx += 200
