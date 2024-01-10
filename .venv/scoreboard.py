from turtle import Turtle

FONT = ("Courier", 40, "bold")

class ScoreBoard(Turtle):

    def __init__(self, coordinate):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(coordinate)
        self.hideturtle()
        self.score = 0
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"{self.score}", False, "center", FONT)

    def update_score(self):
        self.score += 1
        self.write_score()
