import colorgram
from turtle import Turtle, Screen
import random

def extract_colors():
    """Extracts colors from an image by using the colorgram package"""
    colors = colorgram.extract("image.jpeg", 200)
    rgb_colors = []
    for color in colors:
        new_color = (color.rgb.r, color.rgb.g, color.rgb.g)
        rgb_colors.append(new_color)
    return rgb_colors

# TODO: Paint 10 by 10 rows of spots, size 20 paces and spaced by 50 paces

def paint_dots(rows):
    """Paints a grid of dots, rows * rows"""
    colors = extract_colors()
    turtle = Turtle()
    turtle.speed(5)
    turtle.penup()
    turtle.setheading(225)
    turtle.forward(250)
    turtle.setheading(0)
    last_turn = "right"
    for i in range (0,rows):
        turtle.dot(20, random.choice(colors))
        for _ in range(rows-1):
            turtle.forward(50)
            turtle.dot(20, random.choice(colors))
        if last_turn == "right": #go left
            turtle.left(90)
            turtle.forward(50)
            turtle.left(90)
            last_turn = "left"
        else: #go right
            turtle.right(90)
            turtle.forward(50)
            turtle.right(90)
            last_turn = "right"

def main():
    screen = Screen()
    screen.colormode(255)
    paint_dots(10)
    screen.exitonclick()

main()
