from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


def main():
    screen = Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("black")
    screen.title("Pong")

    left_paddle = Paddle("left")
    right_paddle = Paddle("right")

    ball = Ball()

    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(right_paddle.go_up, "Up")
    screen.onkey(right_paddle.go_down, "Down")

    screen.onkey(left_paddle.go_up, "w")
    screen.onkey(left_paddle.go_down, "s")

    game_is_on = True
    while game_is_on:
        time.sleep(ball.move_speed)
        screen.update()
        ball.move()

        #detect wall collision
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()

        #detect paddle collision
        if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() > -320:
            ball.bounce_x()

        #detect if not caught by paddles
        if ball.xcor() > 380:
            ball.reset_position()
            scoreboard.increase_score("l")

        if ball.xcor() < -380:
            ball.reset_position()
            scoreboard.increase_score("r")

    screen.exitonclick()

main()