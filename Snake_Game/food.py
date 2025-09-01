from turtle import Turtle
import random


class Food(Turtle):

  def __init__(self):
    super().__init__()
    self.color('red')
    self.shape('circle')
    self.shapesize(0.5, 0.5)
    self.penup()
    self.appear()

  def appear(self):
    random_x = random.randint(-250, 250)
    random_y = random.randint(-280, 220)
    self.goto(random_x, random_y)
