from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()

def move_forwards():
    turtle.forward(10)

def move_backwards():
    turtle.back(10)

def counter_clockwise():
    turtle.left(10)

def clockwise():
    turtle.right(10)

def clear():
    turtle.reset()

def main():
    """Event listeners"""
    screen.listen()
    screen.onkey(key="w", fun=move_forwards)
    screen.onkey(key="s", fun=move_backwards)
    screen.onkey(key="a", fun=counter_clockwise)
    screen.onkey(key="d", fun=clockwise)
    screen.onkey(key="c", fun=clear)
    screen.exitonclick()

main()