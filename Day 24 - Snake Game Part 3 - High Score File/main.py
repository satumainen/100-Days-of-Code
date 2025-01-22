from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


def main():
    #set up screen
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)
    #create new snake and food object
    new_snake = Snake()
    food = Food()
    scoreboard = Scoreboard()
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

        #detect collision with fod
        if new_snake.head.distance(food) < 15:
            food.refresh()
            new_snake.extend()
            scoreboard.increase_score()

        #detect collision with wall
        if new_snake.head.xcor() > 280 or new_snake.head.xcor() < -280 or new_snake.head.ycor() > 280 or new_snake.head.ycor() < -280:
            scoreboard.reset_highscore()
            new_snake.reset()

        #detect collision with tail with slicing
        for block in new_snake.block[1:]:
            if new_snake.head.distance(block) < 10:
                scoreboard.reset_highscore()
                new_snake.reset()

    screen.exitonclick()



main()