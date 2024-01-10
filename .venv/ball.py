from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.movement_direction_x = 10
        self.movement_direction_y = 10
        self.speed_counter = 0

    def move(self):
        xcor = self.xcor() + self.movement_direction_x
        ycor = self.ycor() + self.movement_direction_y
        self.goto(xcor, ycor)


    def bounce_off_wall(self):
        self.movement_direction_y *= -1

    def bounce_off_paddle(self):
        self.movement_direction_x *= -1
        if self.speed_counter < 5:
            self.speed_counter += 1
            self.movement_direction_x *= 1.25

    def reset_position(self):
        self.goto(0, 0)
        self.speed_counter = 0
