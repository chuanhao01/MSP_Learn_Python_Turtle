import turtle

pen = turtle.Turtle()

# How would you draw a square?
# 1) Walk a certain distance forward
# 2) Turn right (clockwise) for 90 degrees
# 3) Keep repeating Step 1 and 2 four times

square_width = 50

# Instead of repeating the same code 4 times
# Let's use a for loop (used when we want to iterate / repeat code a fixed no. of times)
for i in range(4): # number in range determines number of times we want to loop to repeat
    pen.forward(square_width)
    pen.right(90)
    print(i)

# using loops can save a lot of repetition & redundancy of code, making code shorter

turtle.exitonclick()