from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(0, 270)
        self.reflesh_board()

    def reflesh_board(self):
        self.write(f"Score = {self.score}", font=('Arial', 20, 'normal'))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.reflesh_board()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over !", font=('Arial', 20, 'normal'))
