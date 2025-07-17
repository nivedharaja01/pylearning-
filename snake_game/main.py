import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from turtle import Screen
from  snake_module import Snake
from food_module import Food 
from scoreboard_module import Scoreboard 
import time
 
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    ##for seg in segments:       
        ##seg.forward(20)
    snake.move()


    ##Detect Collision With Food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    ##Detect Collision with wall 
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
       game_is_on = False
       scoreboard.game_over()

    ##Detect collision with tail
    for segment in snake.segments:
         if segment == snake.head:
            pass
         elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

    ##if head collides with any segment in the tail:
    #trigger gameover



 #segments[0].left(90)
screen.exitonclick()
