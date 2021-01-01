import turtle

pen = turtle.Turtle()

# How would you draw a square?
# 1) Walk a certain distance forward
# 2) Turn right (clockwise) for 90 degrees
# 3) Keep repeating Step 1 and 2 four times

square_width = 50

# Instead of using a for loop, let's use a while loop
# while loop is used to repeat code while a condition is true
num_sides_drawn = 0
# We can use the same process to draw a square
# What would be the condition that would tell us that the square is drawn?
while(num_sides_drawn < 4):
    pen.forward(square_width)
    pen.right(90)
    # we increment (add 1) to the num_sides_drawn variable
    num_sides_drawn = num_sides_drawn + 1

turtle.exitonclick()