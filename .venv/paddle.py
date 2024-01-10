from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, coordinate):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.setheading(90)
        self.turtlesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(coordinate)

    def up(self):
        self.forward(30)

    def down(self):
        self.backward(30)