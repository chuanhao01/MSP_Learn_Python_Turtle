import turtle

pen = turtle.Turtle()

# Let's draw something a little more interesting, a 2d grid of squares
# How would you draw a grid of squares?
# For each row in the grid, draw a certain number of squares (number of columns)

square_width = 50
num_rows = 2
num_cols = 2

# Starting X and y coordinate of the turtle pen, so that the pen doesnt draw outside of window
start_x_pos = -(num_cols * square_width) / 2
start_y_pos = (num_rows * square_width) / 2

# use pen.up() to "lift the pen" and stop drawing when moving
pen.up()

# use pen.goto() to set turtle pen to be at that coordinate
pen.goto(start_x_pos, start_y_pos)

# We can use nested for loops, a for loop inside of another for loop
for i in range(num_rows):
    # for each row, we iterate through each column and draw squares
    for j in range(num_cols):
        # use pen.down() to "place the pen on the canvas" and start drawing when moving
        pen.down()
        # this loop draws the square
        for k in range(4): 
            pen.forward(square_width)
            pen.right(90)
        pen.up()
        # move the turtle forward by one square to draw the next one
        pen.forward(square_width)
    # position the turtle to be below the previous row of squares to draw the next row
    pen.goto(start_x_pos, start_y_pos - ((i + 1)* square_width))


turtle.exitonclick()