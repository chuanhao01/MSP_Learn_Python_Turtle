# Setup Turtle
import turtle
pen =  turtle.Turtle()

# Now that you have learnt about parameters, there is just one extra thing you can do on top of this
# This is optional parameters
# Like its name suggests, these parameters are optional, as such they need to have defaults

# Lets think about an example to have this make more sense
# So like the example previously, let's say you want to have the option to change the color of the square as well
# However this might not make sense to do this every single time as we may not want to choose the color every time
# In this case, we would want the color of the square to go back to a default color like black

# The color example continuing from the previous one
# In this case, we can see how the variable color acts as a normal variable, but we can see that it is decalred to have a value
# This would be its default color unless we change it by passing in a different value to the parameters
def draw_square_with_pen_and_color(p, square_length, color='black'):
    # Code that the function will run
    p.color(color) # Set color of the pen
    for _ in range(4): # For each side of the square
        p.forward(square_length) # This pen is from outside the function
        p.right(90)

# How we would call the function
# Let's try calling it the same way as before
# Notice how it still draws the same way with a black sqaure
draw_square_with_pen_and_color(pen, 100)

# But if I add a color as a normal parameter
# We can see that the square drawn is now red
draw_square_with_pen_and_color(pen, 100, 'red')

turtle.exitonclick() # For VSCODE so it does not immdeiately close