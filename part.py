from turtle import Turtle


class Part(Turtle):
    """Represent the defence wall brick"""

    def __init__(self, coordinate):
        super().__init__()
        self.penup()
        self.shapesize(1)
        self.shape("square")
        self.color('white')
        self.goto(
            x=coordinate[0],
            y=coordinate[1])

    def take_hit(self):
        # if (self.distance(bullet_obj) <
        #         10):
        self.destroy_part()
        # return True

    # def hit_by_alien(self, aliens_bullets_list):
    #     pass

    def destroy_part(self):
        self.reset()
        self.hideturtle()
        self.penup()
