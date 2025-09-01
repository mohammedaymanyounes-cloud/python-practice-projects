from turtle import Turtle


class Score(Turtle):


  def __init__(self):
    super().__init__()
    self.color('white')
    self.penup()
    self.l_score = 0
    self.r_score = 0
    self.hideturtle()
    self.update()
    
  def update(self):
    self.clear()
    self.goto(-100,200 )
    self.write(f"{self.l_score}", align="center", font="courier,100,normal")
    self.goto(100,200 )
    self.write(f"{self.r_score}", align="center", font="courier,100,normal")
    self.goto(0,280)
    self.write("Score", align="center", font="Courier,40,normal")

  

  
