from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.update_score(0)
    
    def update_score(self, value):
        self.clear()
        self.write(f"Score: {value}", align="center", font=("Arial", 24, "normal"))
