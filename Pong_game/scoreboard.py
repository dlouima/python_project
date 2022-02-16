from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.goto(-100, 200)
        self.reflesh_scoreboard()

    def reflesh_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align='center',
                   font=('Courier', 60, 'normal'))
        self.goto(100, 200)
        self.write(self.r_score, align='center',
                   font=('Courier', 60, 'normal'))

    def r_score_point(self):
        self.r_score += 1
        self.reflesh_scoreboard()

    def l_score_point(self):
        self.l_score += 1
        self.reflesh_scoreboard()
