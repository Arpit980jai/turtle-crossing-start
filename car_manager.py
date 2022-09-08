from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.allCars=[]

    def create_car(self,speed):
        self.randomChoice=random.randint(1,speed)
        if self.randomChoice ==1:
            car=Turtle()
            car.shape("square")
            car.shapesize(stretch_wid=1,stretch_len=2)
            car.color(random.choice(COLORS))
            car.penup()
            random_y=random.randint(-250,250)
            car.goto(300,random_y)
            self.allCars.append(car)

    def move_car(self):
        for car in self.allCars:
            car.backward(STARTING_MOVE_DISTANCE)




