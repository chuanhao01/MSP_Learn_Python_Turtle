# This is how a list is made in pyton
# We can also assign it to a variable
l = []

# For a list, you can think of it as a sequentially container
# Anything you put in is part of a sequence and has a place number (It is called index)

# Example the sequence of natural numbers, 1, 2, 3, 4, 5
# We can see that 1 is first followed by 2, and so on
# This seqence can also be any number like 3, 2, 6
# Then the first number is 3, followed by 2 and so on

# A list is similar to this in the sense that it can have integers or strings
# So if we made a list like this [1, 2, 3, 4, 5]
# In place of first, second, third, we use its index (Basically meaning its position)
l = [1, 2, 3, 4, 5] 
print(l) # To show the list
print(l[0]) # Now a special thing in programming and index is that for the first place, its actually position 0
print(l[1]) # Then for second it is position 1 and so on

# Special thing about python is that the position can be backwards
print(l[-1]) # For the last position, it is -1 (not -0 because that is 0)

# Example with strings
l = ['a', 'b', 'c', 'd', 'e']
print(l)
print(l[0]) # First item in the list, postion 0
print(l[1])

print(l[-1])
