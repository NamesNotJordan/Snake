import time
from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Turtle")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up,"w")
screen.onkey(snake.down,"s")
screen.onkey(snake.left,"a")
screen.onkey(snake.right,"d")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    #  food collision
    if snake.head.distance(food) <15:
        food.refresh()
        snake.grow()
        scoreboard.add_to_score()
    # Wall Collision
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on = False
        scoreboard.game_over()
    # Tail Collision
    for segment in snake.segments[1::]:
        if snake.head.distance(segment) <10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()