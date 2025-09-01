from turtle import Turtle , Screen
from paddle import Paddle
from ball import Ball
import time
from score import Score


screen=Screen()
r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
ball=Ball()
score=Score()


screen.bgcolor("black")
screen.setup(800,600)
screen.title("ping pong")
screen.listen()
screen.onkey(r_paddle.up,"Up")
screen.onkey(r_paddle.down,"Down")
screen.onkey(l_paddle.up,"w")
screen.onkey(l_paddle.down,"s")
screen.tracer(0)

default_sleep=.1
game_on=True
while game_on:
    screen.update()
    time.sleep(default_sleep)
    ball.goto(ball.xcor()+ball.x_move,ball.ycor()+ball.y_move)
    #لو خرجت من فوق او تحت    
    if ball.ycor()>=280 or ball.ycor()<=-280:
        ball.y_move*=-1
#خبط في المضرب
    if ball.xcor()>=330 and ball.distance(r_paddle)<=50 or ball.xcor()<=-330 and ball.distance(l_paddle)<=50:
        ball.x_move*=-1 
        default_sleep*=0.9
        

#لو خرجت من اليمين او اليسار        

    if ball.xcor()>=400:
        ball.goto(0,0)
        ball.x_move*=-1
        score.l_score+=1
        score.update()
        default_sleep=0.1

    if ball.xcor()<=-400:
        ball.goto(0,0)
        ball.x_move*=-1
        score.r_score+=1
        score.update()
        default_sleep=0.1


screen.exitonclick()
