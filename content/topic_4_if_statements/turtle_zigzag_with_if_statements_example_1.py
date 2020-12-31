import turtle

# Let's do some zigzag lines with turtle
pen = turtle.Turtle()

# Let's do 10 zigzags
num_zigzags = 10

for i in range(num_zigzags):
    pen.setheading(0) # Set the pen to face east
    # the "%" means remainder, so i % 2 == 0 checks if i is even number or not
    # even numbers when divided by 2 does not have any remainder, aka remainder = 0
    if i % 2 == 0: 
        pen.left(45)
        pen.forward(50)
    else:
        pen.right(45)
        pen.forward(50)

turtle.exitonclick()