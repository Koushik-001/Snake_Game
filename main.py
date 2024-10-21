# import csv
# with open('Walmart_sales.csv') as dataFile:
#        data = csv.reader(dataFile)
#        temp = []
#        for i in data:
#               print(i[0])

# import pandas

# data = pandas.read_csv("squirells.csv")
# new_dict={
#     "fur_color":["Gray","Red","Black"],
#         "count":[len(data[data["Primary Fur Color"] == "Gray"]),len(data[data["Primary Fur Color"] == "Red"]),len(data[data["Primary Fur Color"] == "Black"])]
# }
# print(pandas.DataFrame(new_dict))

# from turtle import Turtle,Screen
# import random

# new_turtle = Turtle()
# def turtle_fun(sides):
#     angle = 360/sides
#     for i in range(sides):
#         new_turtle.forward(50)
#         new_turtle.right(angle)

# color = ['violet','indigo','blue','green','yellow','orange','red']
# for i in range(3,11):
#     new_turtle.speed(10)
#     new_turtle.color(random.choice(color))
#     turtle_fun(i)
# new_screen = Screen()
# new_screen.exitonclick()

# from turtle import Turtle, Screen
# from random import randint

# # Set up the screen and enable RGB color mode
# new_screen = Screen()
# new_screen.colormode(255)  # Allow colors to be set with RGB values

# new_turtle = Turtle()
# new_turtle.speed('fastest')

# # Draw a spirograph by rotating in steps of 10 degrees
# for _ in range(int(360 / 10)):  # 360 degrees divided by 10-degree steps
#     r = randint(0, 255)  # Generate random red value
#     g = randint(0, 255)  # Generate random green value
#     b = randint(0, 255)  # Generate random blue value
#     new_turtle.color(r, g, b)  # Set the turtle color to a random RGB value
#     new_turtle.circle(100)  # Adjust the radius of the circle as needed
#     new_turtle.penup()
#     new_turtle.setheading(new_turtle.heading() + 10)  # Rotate by 10 degrees
#     new_turtle.pendown()

# new_screen.exitonclick()

# from turtle import Turtle,Screen

# new_turtle = Turtle()
# new_screen = Screen()

# def triangle_fun():
#     for i in range(3):
#         new_turtle.forward(50)
#         new_turtle.right(120)
    
# heading = new_turtle.heading()
# while(new_turtle.heading() != heading):
#     new_turtle.speed("fastest")
#     new_turtle.setheading(new_turtle.heading()+10)
#     triangle_fun()
# new_screen.exitonclick()

# import colorgram

# rgb_list = []
# colors = colorgram.extract('painting.jpg',20)
# for i in colors:
#     r = i.rgb.r
#     g = i.rgb.g
#     b = i.rgb.b
#     colors_tuple = (r,g,b)
#     rgb_list.append(colors_tuple)
# print(rgb_list)

# from turtle import Turtle,Screen
# import random

# colors_array = [(202, 164, 110),(149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77)]
# new_turtle = Turtle()
# new_turtle.speed('fastest')
# new_turtle.hideturtle()
# new_screen = Screen()
# new_screen.colormode(255)

# def color_fun():
#     for _ in range(10):  
#         new_turtle.dot(20,random.choice(colors_array))
#         new_turtle.penup()
#         new_turtle.forward(50)
#         new_turtle.pendown()
# X = -250
# Y = -250

# for i in range(10):
#     new_turtle.penup()
#     new_turtle.goto(X,Y)
#     new_turtle.pendown()
#     color_fun()
#     Y+=50

    

# new_screen.exitonclick()

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