from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.score=0
        self.hideturtle()
        self.update()
    def update(self):
        self.clear()
        self.goto(0,250)   
        self.write(f"Score:,{self.score}",align="center",font=("Courier",24,"normal")) 
    def increase(self,points):
        self.score+=points
        self.update()
    def reset(self):
        self.score=0
        self.update()
    def game_over(self):
        self.goto(0,0)
        self.write(f"Game over",align="center",font=("Courier",24,"normal"))        
