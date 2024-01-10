from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

# creates screen setup and layout
screen = Screen()
screen.screensize(800, 600, "black")
screen.title("Pong")
screen.tracer(0)

# creates paddle objects and puts them where they should be accordingly on the screen
paddle_coordinates = (350, 0), (-350, 0)
r_paddle = Paddle(paddle_coordinates[0])
l_paddle = Paddle(paddle_coordinates[1])

# creates ball object
ball = Ball()

# creates scoreboard objects and put them where should be located accordingly
scoreboard_coordinates = (40, 250), (-40, 250)
r_scoreboard = ScoreBoard(scoreboard_coordinates[0])
l_scoreboard = ScoreBoard(scoreboard_coordinates[1])

# listen for user inputs on the keyboard to move the paddles
screen.listen()
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")


# runs the game
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    ball.move()

    # bounces the ball off of the horizontal walls when it impacts them
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_off_wall()

    # bounces the ball off of the paddle when it imapcts them
    if ball.distance(r_paddle) <= 50 and ball.xcor() > 320 or ball.distance(l_paddle) <= 50 and ball.xcor() < -320:
        ball.bounce_off_paddle()

    # resets ball to starting position, set its speed to the default speed, changes the direction of the ball, as well
    # as updates the score
    if ball.xcor() > 380:
        ball.reset_position()
        ball.movement_direction_x = -10
        l_scoreboard.update_score()

    if ball.xcor() < -380:
        ball.reset_position()
        ball.movement_direction_x = 10
        r_scoreboard.update_score()

screen.exitonclick()