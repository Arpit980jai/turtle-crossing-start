from turtle import Turtle,Screen
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.left(90)
        self.goto(STARTING_POSITION)
        self.game_over=False
        self.move_up()

    def move_up(self):
        self.forward(MOVE_DISTANCE)
    def move_down(self):
        self.backward(MOVE_DISTANCE)

    def check_finish_line(self):
        if self.ycor()>=280:
            game_over=True
    def reset(self):
        self.goto((STARTING_POSITION))



