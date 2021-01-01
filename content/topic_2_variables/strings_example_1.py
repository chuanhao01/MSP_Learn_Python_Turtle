# Variables are just some name for some value
# Let's start with string, which is just some text
# "=" operator means assignment
msg = "Hello, I am "

# Why variables?
# Nice way to reference something, especially if that something is very long
print(msg + "David")
print(msg + "Sally")

# Notice that the variable msg was used 
# instead of the direct string "Hello I am" in the print statements above
# thus, there was no need to keep typing "Hello I am"

# Concatenation can be done in conjunction with assignment
msg = msg + "David" 
# Take current string value of variable msg and combine it with the string "David"
# Use that new combined string and assign it to the variable msg
print(msg) # Should output "Hello, I am David" in the console