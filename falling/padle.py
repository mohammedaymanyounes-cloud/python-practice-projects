from turtle import Turtle

class Padle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(1,5)
        self.goto(0,-280)

    def left(self):
        new_x= self.xcor()-40
        if new_x>-350:
            self.goto(new_x,self.ycor())
    def right(self):
        new_x=self.xcor()+40
        if new_x<350:
            self.goto(new_x,self.ycor())


        
