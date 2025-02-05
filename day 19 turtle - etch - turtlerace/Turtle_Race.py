from turtle import *
import random

race = False
all_turtles = []

screen = Screen()
screen.setup(width=600, height=600)
input = screen.textinput(title="Place your bet", prompt="Red, Green, Blue, Yellow, or Purple are racers, which turtle will win?")  # Kept 'input' as requested
print(f"{input} is the turtle the user has bet on. Let's see how this turns out.")

colors = ['red', 'green', 'blue', 'yellow', 'purple']
pos = [-100, -50, 0, 50, 100]  # Kept 'pos' as requested

for i in range(0, 5):
    t = Turtle(shape="turtle")  # Kept 't' as requested
    t.penup()
    t.color(colors[i])
    t.goto(x=-290, y=pos[i])  # Using 'pos'
    all_turtles.append(t)

if input:
    race = True

while race:
    for t in all_turtles:
        travelled_dist = random.randint(0, 10)
        t.forward(travelled_dist)
        if t.xcor() > 290:
            race = False
            winning_color = t.pencolor()
            if winning_color == input.lower():
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
            screen.bye()
            break 
