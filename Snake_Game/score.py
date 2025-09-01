from turtle import Turtle


class Score_board(Turtle):

  def __init__(self):
    super().__init__()
    self.color('white')
    self.penup()
    self.score = 0
    self.highscore=self.get_highscore()
    self.hideturtle()
    self.goto(-350,200 )
    self.update()

  def get_highscore(self):
    with open('highscore.txt',"r") as file:
      return int(file.read())
  def save_highscore(self):
    with open("highscore.txt","w") as file:
      file.write(str(self.highscore))    



  def update(self):
    self.write(f"Score : {self.score}   High score: {self.highscore} ", align="center", font="Arial,24,normal")

  def increase(self):
    self.score += 1
    self.clear()
    self.update()

  def game_over(self):
    self.clear()
    self.screen.bgcolor("darkred")
    self.goto(0, 0)
    if self.score>self.highscore:
      self.highscore=self.score
      self.save_highscore()  
    self.write(f"---------Game Over---------\n\n your score : {self.score}\n\n High score: {self.highscore}",
               align="center",
               font=("Arial,24,normal"))
