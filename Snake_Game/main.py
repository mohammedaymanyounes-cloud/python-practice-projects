from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from score import Score_board
window = Screen()
window.bgcolor('black')
window.setup(800, 800)
window.tracer(0)

sam = Snake()
food=Food()
score=Score_board()

game_on = True
while game_on:
  for segmant in sam.turtles[:-1]:
    if sam.head.distance(segmant)<5:
      game_on=False
      score.game_over()
      
  sam.move()
  window.update()
  time.sleep(.1)
  window.listen()
  window.onkey(sam.up, "Up")
  window.onkey(sam.down, "Down")
  window.onkey(sam.right, "Right")
  window.onkey(sam.left, "Left")
  if sam.head.distance(food)<15:
    food.appear()
    sam.extend()
    score.increase()
  if sam.head.xcor()>380 or sam.head.xcor()<-380 or sam.head.ycor()>220 or sam.head.ycor()<-320:
    game_on=False
    score.game_over()
window.exitonclick()
