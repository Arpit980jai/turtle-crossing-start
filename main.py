import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
arpit=Player()
cars=CarManager()
score=Scoreboard()


screen.listen()
screen.onkey(arpit.move_up,"Up")
screen.onkey(arpit.move_down,"Down")

speed=10
scores=0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car(speed)
    cars.move_car()
    for car in cars.allCars:
        if car.distance(arpit) < 20:
            game_is_on=False
            score.game_over()
    if arpit.ycor()>250:
        arpit.reset()
        speed-=1
        cars.create_car(speed)
        print(speed)
        scores+=1
        score.update_Scoreboard(scores)




screen.exitonclick()








screen.exitonclick()