from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
screen = Screen()
screen.setup(width= 600, height= 600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard(0)
screen.listen()
screen.onkey(snake.left,"a")
screen.onkey(snake.right,"d")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.1)
    snake.move()

    # Detect collition with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.add()

    # Detect collition with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.game_over()
        game_is_on = False

    # Detect collition with wall
    for segment in snake.snake_body[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()

