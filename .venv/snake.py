from turtle import Turtle
X_POSITION = [0,-20,-40]
MOVE_DISTANCE = 20
class Snake:

    def __init__(self):
        self.snake_body = []
        self.create_snake()

    def create_snake(self):
        # Creates Snake
        for t in range(3):
            body_part = Turtle(shape="square")
            body_part.penup()
            body_part.color("white")
            body_part.goto(x=X_POSITION[t], y=0)
            self.snake_body.append(body_part)
    def move(self):
        #  Moves snake
        for seg_num in range(len(self.snake_body) - 1, 0, -1):
            new_X = self.snake_body[seg_num - 1].xcor()
            new_Y = self.snake_body[seg_num - 1].ycor()
            self.snake_body[seg_num].goto(new_X, new_Y)
        self.snake_body[0].forward(MOVE_DISTANCE)