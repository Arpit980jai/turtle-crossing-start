from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
            super().__init__()
            timmy=Turtle()
            timmy.color("black")
            timmy.penup()
            timmy.hideturtle()
            self.update_Scoreboard(scores=0)


    def update_Scoreboard(self,scores):
            self.penup()
            self.hideturtle()
            self.clear()
            self.goto(-270, 270)
            print(scores)
            self.write(scores, align="center", font=("Arial", 20, "normal"))
    def game_over(self):
            self.penup()
            self.hideturtle()

            self.goto(0, 0)

            self.write("Game Over", align="center", font=("Arial", 40, "normal"))

