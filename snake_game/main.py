from turtle import Turtle,Screen
from snake import Snake
from food import Food
from score_board import Scoreboard
import random
import time
screen=Screen()
screen.setup(600,600)
screen.bgcolor('black' )
screen.title("my snake game")
screen.tracer(0)

snake=Snake()
food=Food()
scoreboard=Scoreboard()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")
game_on=True

while game_on:
    screen.update()
    time.sleep(0.1) 
    snake.move()
    

    #detect collision with food

    if snake.all_snake[0].distance(food)<15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #detect collision with walls
        
    if snake.all_snake[0].xcor()>290 or snake.all_snake[0].xcor() < -290 or snake.all_snake[0].ycor() >290 or snake.all_snake[0].ycor() <-290:
        scoreboard.reset()
        snake.reset()

    #detect tails

    for i in snake.all_snake[3:]:
        if snake.all_snake[0].distance(i)<10:
            scoreboard.reset()
            snake.reset()



screen.exitonclick()