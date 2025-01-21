from turtle import Turtle, Screen
import random

def create_turtles():
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    turtles = []
    for color in colors:
        new_turtle = Turtle(shape="turtle")
        new_turtle.shape("turtle")
        new_turtle.color(color)
        turtles.append(new_turtle)
    return turtles

def place_turtles(turtles):
    start_height = -75
    for turtle in turtles:
        turtle.penup()
        turtle.goto(-230, start_height)
        start_height += 30

def move_turtles(turtles):
    is_race_on = True
    while is_race_on:
        for turtle in turtles:
            random_distance = random.randint(0,10)
            turtle.forward(random_distance)
            if turtle.xcor() > 230:
                return turtle

def main():
    screen = Screen()
    screen.setup(width=500, height=400)
    user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
    turtles = create_turtles()
    place_turtles(turtles)
    winner = move_turtles(turtles)
    result = winner.pencolor()
    if user_bet.lower() == str(result).lower():
        print(f"You won! The winner is {str(result)}")
    else:
        print(f"You lost! The winner is {str(result)}")
    screen.exitonclick()

main()






