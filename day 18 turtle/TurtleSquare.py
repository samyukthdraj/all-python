from turtle import *

message = ("pink turtle")
print (f"hello {message}")

turtlepink= Turtle()
turtlepink.shape("turtle")
turtlepink.color("pink")

for i in range(4):
    # turtlepink.goto(30,50)
    turtlepink.forward(200)
    turtlepink.right(90)

# ctrl + h for find and replace, then ctrl alt enter to replace all 

screen = Screen()



screen.exitonclick()

