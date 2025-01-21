import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


def main():

    screen = Screen()
    screen.setup(width=600, height=600)
    screen.tracer(0)

    #create objects
    player = Player()
    car_manager = CarManager()
    scoreboard = Scoreboard()

    #event listener
    screen.listen()
    screen.onkey(player.move, "Up")


    game_is_on = True
    while game_is_on:
        time.sleep(0.1) #cycle speed
        screen.update()
        #creates a new random car each game cycle
        car_manager.create_car()
        car_manager.move_cars()

        #detect collision with car
        for car in car_manager.all_cars:
            if car.distance(player) < 20:
                game_is_on = False
                scoreboard.game_over()

        if player.is_at_finish_line():
            player.go_to_start()
            scoreboard.increase_level()
            car_manager.level_up()



    screen.exitonclick()

main()
