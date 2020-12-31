import turtle

pen = turtle.Turtle()

# How would you draw a square?
# 1) Walk a certain distance forward
# 2) Turn right (clockwise) for 90 degrees
# 3) Keep repeating Step 1 and 2 four times

square_width = 50

pen.forward(square_width)
pen.right(90)

pen.forward(square_width)
pen.right(90)

pen.forward(square_width)
pen.right(90)

pen.forward(square_width)
pen.right(90)

turtle.exitonclick()