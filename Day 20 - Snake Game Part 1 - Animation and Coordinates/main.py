from turtle import Turtle, Screen
from snake import Snake
import time


def main():
    #set up screen
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)
    #create new snake object
    new_snake = Snake()
    #event listening
    screen.listen()
    screen.onkey(new_snake.up, "Up")
    screen.onkey(new_snake.down,"Down")
    screen.onkey(new_snake.left, "Left")
    screen.onkey(new_snake.right, "Right")

    screen.update()

    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1) #
        new_snake.move()

    screen.exitonclick()



main()