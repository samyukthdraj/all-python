from turtle import Turtle
import random
turtle1= Turtle()
colors = ["Cornflower Blue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw(sides):
    for i in range(sides):
        angle = 360/sides
        turtle1.forward(100)
        turtle1.right(angle)

for j in range (3,11):
    turtle1.color(random.choice(colors))
    draw(j)
