from turtle import Turtle
STARTING_POSITIONS = STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

MOVE_DISTANCE = 20
class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        # Creates Snake
        for position in STARTING_POSITIONS:
            self.add_segment(position)
    def add_segment(self, position):
        body_part = Turtle(shape="square")
        body_part.penup()
        body_part.color("white")
        body_part.goto(position)
        self.snake_body.append(body_part)
    def extend(self):
        # Add a new segment ot the snake
        self.add_segment(self.snake_body[-1].position())

    def move(self):
        #  Moves snake
        for seg_num in range(len(self.snake_body) - 1, 0, -1):
            new_X = self.snake_body[seg_num - 1].xcor()
            new_Y = self.snake_body[seg_num - 1].ycor()
            self.snake_body[seg_num].goto(new_X, new_Y)
        self.head.forward(MOVE_DISTANCE)

    # To move +30 left -30 Right
    def left(self):
        self.head.left(90)
    def right(self):
        self.head.right(90)

