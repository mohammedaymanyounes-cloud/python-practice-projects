from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.y_move=-10
        self.shapes=["square","circle","turtle","triangle","square"]
        self.colors=["green","red","blue","purple","yellow"]
        self.reset_position()

    def move(self):
        self.goto(self.xcor(),self.ycor()+self.y_move)    
    def reset_position(self):
        random_x=random.randint(-350,350)  
        self.goto(random_x,250)  

        random_shape=random.choice(self.shapes)  
        self.shape(random_shape)

        if random_shape=="turtle" and random.randint(1,10)==1:
            self.color("white")
        else:
            self.color(random.choice(self.colors))

        random_size=random.uniform(.5,2)
        self.shapesize(random_size,random_size)        
 
