from turtle import Turtle, Screen, color
import random
import turtle
import time

window = Screen()
window.setup(600, 400)
window.bgcolor('white')
window.title('Turtles race')
choice=window.textinput('let`s gamble', 'choose a color from those (Red,blue,black)')
"""make lists"""
colors = ['red', 'blue', 'black']
y_position = [70, 0, -70]
turtles = []
"""make turtles"""
for i in range(3):
  new_turtle = Turtle(shape='turtle')
  new_turtle.color(colors[i])
  new_turtle.penup()
  new_turtle.goto(x=-280, y=y_position[i])
  turtles.append(new_turtle)

def display(winner):
  if winner==choice:
    window.bgcolor('blue')
    turtle.pencolor('black')
    turtle.write('You won!',font=('arial',35,'normal'))
    time.sleep(5)

  else:
    window.bgcolor('red')
    turtle.pencolor('green')
    turtle.write('You lost!',font=('arial',35,'normal'))
    time.sleep(5)

def race():
  game_on = True
  while game_on:
    for turtle in turtles:
      if turtle.xcor() > 280:
        game_on = False
        winner = turtle.pencolor()
        display(winner)
      else:
        turtle.forward(random.randint(1, 5))
race()
