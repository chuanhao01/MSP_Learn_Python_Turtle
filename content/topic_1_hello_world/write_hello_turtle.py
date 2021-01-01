import turtle

# set the screen height and width to 100% 
# of our screen height and width
turtle.Screen().setup(width=1.0, height=1.0)

# Write hello world using turtle
turtle.write(
    "Hello World", 
    font=('Verdana', 16, 'italic'), 
    align='center'
)

# Hide turtle
turtle.hideturtle()

# to keep the screen on in vscode
turtle.Screen().mainloop()
