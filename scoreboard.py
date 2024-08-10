from turtle import Turtle

FONT = ('Arial', 12, 'bold')


class ScoreBoard(Turtle):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.score = -1
        self.hideturtle()
        self.penup()
        self.goto(x=-(screen_width / 2) + 10, y=(screen_height / 2) - 30)
        self.color('white')
        self.update_score()

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(arg=f"Score: {self.score}", align='left', font=FONT)
        # self.write(arg=f"RANA", align='left', font=FONT)

    def game_over(self):
        # self.clear()
        self.goto(x=0, y=0)
        self.write(arg=f"Game Over", align='center', font=('Arial', 22, 'normal'))
