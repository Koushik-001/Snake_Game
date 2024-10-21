from turtle import Turtle,Screen
import time
from snake import Snake 
from food import Food
from scoreboard import Scoreboard
new_turtle = Turtle()
new_screen = Screen()
new_snake = Snake()
new_food = Food()
new_scoreboard = Scoreboard()
new_screen.colormode(255)
new_screen.bgcolor("black")
new_screen.setup(width=600, height=600) 
new_screen.tracer(0)

new_screen.listen()
new_screen.onkey(new_snake.up,"Up")
new_screen.onkey(new_snake.down,"Down")
new_screen.onkey(new_snake.left,"Left")
new_screen.onkey(new_snake.right,"Right")

game_on = True
count=0
while game_on:
    new_screen.update() 
    time.sleep(0.1)
    new_snake.move()
    if new_snake.head.distance(new_food)<15:
        count+=1
        new_scoreboard.update_score(count)
        new_snake.extend()
        new_food.refresh()
    if new_snake.head.xcor()<-280 or new_snake.head.xcor()>280 or new_snake.head.ycor()<-280 or new_snake.head.xcor()>280:
        game_turtle = Turtle()
        game_turtle.hideturtle()
        game_turtle.color("white")
        game_turtle.penup()
        game_turtle.goto(-40,0)
        game_turtle.write(arg="Game Over",font=(30))
        game_on = False
        
    for i in new_snake.segment[1:]:
        if new_snake.head.distance(i) < 10:
           game_turtle = Turtle()
           game_turtle.hideturtle()
           game_turtle.color("white")
           game_turtle.penup()
           game_turtle.goto(-40,0)
           game_turtle.write(arg="Game Over",font=(30))
           game_on = False
           
new_screen.exitonclick()
