# What are if statements?
# basically checking if a condition is true, 
# if so, then do something
# if not, then don't do something or do something else

x = 10

if x == 10: # since x is equal to 10, "x is 10" would appear
    print("x is 10")
# Note that "==" is used to check if a variable is equal to a certain value, like above

# What if you want to do something else if a condition is not true?
# you can use if-else 
if x == 100:
    print("x is 100")
else:
    print("x is not 100") # should be printed 
# since x is not 100, x is 10, so x == 100 is false
# thus, "x is not 100" would be printed