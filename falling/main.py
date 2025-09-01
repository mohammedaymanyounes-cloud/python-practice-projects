from turtle import Turtle , Screen
import time
from padle import Padle
from ball import Ball
from score import Score

screen=Screen()
padle=Padle()
ball=Ball()
score=Score()

screen.setup(800,600)
screen.bgcolor("black")
screen.title('Falling')
screen.tracer(0)

screen.listen()
screen.onkey(padle.right,"Right")
screen.onkey(padle.left,"Left")

game_on=True
game_speed=0.1

while game_on:
   screen.update()
   time.sleep(game_speed)   
   ball.move()


   if ball.distance(padle)<50 and ball.ycor()<230:
      shape_type=ball.shape()
      shape_color=ball.color()[0]
      if shape_type=='turtle':
         if shape_color=='white':
            game_on=False
            score.game_over()
         else:
           points=5
           score.increase(points)
      elif shape_type=='circle':
         points=1
         score.increase(points)
      elif shape_type=='square':
         points=2
         score.increase(points)
      elif shape_type=='triangle':
         score.reset()
      ball.reset_position()
      game_speed*=.9 
   if ball.ycor()<-300:
      ball.reset_position()     






screen.exitonclick()

