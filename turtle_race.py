from turtle import *
import random

turtle1 = Turtle()
turtle2 = Turtle()
turtle3 = Turtle()
scr = turtle1.getscreen()
turtle1.speed(0)
turtle1.penup()
turtle2.penup()
turtle3.penup()
turtle1.goto(-150, 200)
finish_line = -150 + 20*17
for i in range(20):
    turtle1.pendown()
    turtle1.write(i)
    turtle1.right(90)
    turtle1.forward(150)
    turtle1.left(180)
    turtle1.forward(150)
    turtle1.right(90)
    turtle1.penup()
    turtle1.forward(20)

turtle1.goto(-150, 170)
turtle1.color("red")
turtle1.shape("turtle")
turtle2.color("yellow")
turtle2.shape("turtle")
turtle2.goto(-150, 140)
turtle3.color("green")
turtle3.shape("turtle")
turtle3.goto(-150, 110)
turtle1_pos = -150
turtle2_pos = -150
turtle3_pos = -150

turtle1.pendown()
turtle2.pendown()
turtle3.pendown()


while turtle1_pos < finish_line or turtle2_pos < finish_line or turtle3_pos <  finish_line:
    turtle1_ran = random.random() * 5
    turtle2_ran = random.random() * 5
    turtle3_ran = random.random() * 5
    turtle1_pos += turtle1_ran
    turtle2_pos += turtle2_ran
    turtle3_pos += turtle3_ran
    turtle1.forward(turtle1_ran)
    turtle2.forward(turtle2_ran)
    turtle3.forward(turtle3_ran)



done()



