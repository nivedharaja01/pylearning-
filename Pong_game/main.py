from turtle import Screen, Turtle
from paddle_module import Paddle 
from ball import Ball
from scoreboard_module import Scoreboard
import time

screen = Screen()

screen.bgcolor("black")
screen.setup(width=600,height=600)
screen.title("Pong")
screen.tracer(0)


r_paddle = Paddle((260,0))
l_paddle = Paddle((-260,0))

ball = Ball()
scoreborad = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.ball_move()

#detect collision with wall
#if ball.ycor() > 270 or ball.ycor() < -270:
      #ball.bounce()

    print(ball.xcor(), ball.ycor())

    if ball.ycor() > 280 or ball.ycor() < -280:
          ball.bounce_y()  # vertical bounce

    if ball.xcor() > 280 or ball.xcor() < -280:
           ball.bounce_x()  # horizontal bounce

    #Detect collision with r_paddle
    #if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
            #ball.bounce_x()
       
    #if ball.distance(l_paddle)<50 and ball.xcor() < -320:
            #ball.bounce_x()

    # Right paddle
    if ball.xcor() > 240 and ball.distance(r_paddle) < 50:
           ball.bounce_x()

# Left paddle
    if ball.xcor() < -240 and ball.distance(l_paddle) < 50:
            ball.bounce_x()
     
   # Ball missed right paddle
    if ball.xcor() > 280:
       ball.reset_position()
       scoreborad.l_point()
    # You can also add score logic here

# Ball missed left paddle
    if ball.xcor() < -280:
       ball.reset_position()
       scoreborad.r_point()
 
screen.exitonclick()

