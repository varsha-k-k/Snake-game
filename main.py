from turtle import  Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

screen = Screen()


screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("snake here!")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()


screen.listen()
screen.onkey(snake.up , "Up")
screen.onkey(snake.down , "Down")
screen.onkey(snake.left ,"Left")
screen.onkey(snake.right , "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

    if snake.head.distance(food)< 15:
        food.refresh()
        snake.extend_segment()
        score.increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset()
        snake.reset()

    for segment in snake.segments[1:]:
        # if segment == snake.head():
        #     pass
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()
screen.exitonclick()
