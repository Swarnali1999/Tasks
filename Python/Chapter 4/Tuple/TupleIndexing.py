# A tuple is an immutable (can’t change or modified) data type in Python.
# Once defined, tuple elements can’t be manipulated or altered.
# We create tuple using ().

# Example of empty tuple
a = ()  
print(a)            

# Tuple with only one element needs a comma.
a1 = (1,)          

# Example of Tuple with more than one element
a2 = (1, 7, 2)  

# printing elements of a tuple
print(a2[2])

# We cannot update the values of a tuple
a2[0]=4
print(a2)