# import turtle

# # Screen setup
# screen = turtle.Screen()
# screen.setup(width=600, height=600)  # Set window size

# # Turtle setup
# my_turtle = turtle.Turtle()
# my_turtle.speed(0)  # Set speed to fastest

# # Movement functions
# def move_forward():
#     my_turtle.forward(20)

# def move_backward():
#     my_turtle.backward(20)

# def turn_left():
#     my_turtle.left(90)  # Adjust rotation angle as needed

# def turn_right():
#     my_turtle.right(90)  # Adjust rotation angle as needed

# def clear_screen():
#     my_turtle.clear()

# def exit_program():
#     screen.bye()


# # Key bindings
# screen.listen()
# screen.onkey(move_forward, "w")
# screen.onkey(move_backward, "s")
# screen.onkey(turn_left, "a")
# screen.onkey(turn_right, "d")
# screen.onkey(clear_screen, "c")
# screen.onkey(exit_program, "Escape")  # Or "Esc"


# screen.mainloop()


import turtle 
screen= turtle.Screen()
screen.setup (width=600, height=600)

t=turtle.Turtle()
t.speed(0)

def left():
    t.left(10)

def right():
    t.right(10)

def forward():
    t.forward(20)

def backward():
    t.backward(20)
def exit():
    screen.bye()
def clear():
    t.clear()
    t.penup()
    t.home()
    t.pendown()

screen.listen()
screen.onkey(forward, "w")         
screen.onkey(backward, "s")         
screen.onkey(left, "a")         
screen.onkey(right, "d")  
screen.onkey(exit, "Escape")  
screen.onkey(clear, "c")

screen.mainloop()