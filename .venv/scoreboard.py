from turtle import Turtle
FONT = ["courier", 24, "normal"]

class Scoreboard(Turtle):


    def __init__(self, score):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("White")
        self.penup()
        self.goto(0,265)
        self.write(arg= f"Score: {self.score}", align= "center",font= FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(arg="GAME OVER", align="center", font=FONT)

    def add(self):
        self.clear()
        self.score += 1
        self.write(arg=f"Score: {self.score}", align="center", font=FONT)

