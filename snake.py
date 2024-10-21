from turtle import Turtle

POS_ARR = [(0,0),(-20,0),(-40,0)]
FORWARD = 20
RIGHT=0
UP=90
DOWN=270
LEFT=180

class Snake:
    def __init__(self) -> None:
        self.segment = []
        self.creat_snake()
        self.head = self.segment[0]
        
    def creat_snake(self):
        for i in POS_ARR:
            self.add_segment(i)
            
    def add_segment(self,position):
            new_turtle = Turtle()
            new_turtle.shape("square")
            new_turtle.color("white")
            new_turtle.penup()
            new_turtle.goto(position)
            self.segment.append(new_turtle)
            
    def extend(self):
        self.add_segment(self.segment[-1].position())
            
    def move(self):
            for seg in range(len(self.segment)-1,0,-1):
                new_x = self.segment[seg-1].xcor() 
                new_y = self.segment[seg-1].ycor() 
                self.segment[seg].goto(new_x,new_y)
            self.segment[0].forward(FORWARD)
            
    def up(self):
        if self.head.heading() != DOWN:
           self.segment[0].setheading(UP)
        
    def down(self):
        if self.head.heading() != UP: 
           self.segment[0].setheading(DOWN)
    
    def left(self):
        if self.head.heading() != RIGHT:
           self.segment[0].setheading(LEFT)
    
    def right(self):
        if self.head.heading() != LEFT:
           self.segment[0].setheading(RIGHT)