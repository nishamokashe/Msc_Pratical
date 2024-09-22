
''' Demonstrate string formatting using replacement operator{} '''

name = "Alice"
age = 30

# Using {} as placeholders
formatted_string = "My name is {} and I am {} years old.".format(name, age)
print(formatted_string)

#Positional and Keyword Arguments

formatted_string = "The {0} is {1} years old. {0} is very talented.".format(name, age)
print(formatted_string)

# Keyword Arguments

formatted_string = "My name is {name} and I am {age} years old.".format(name=name, age=age)
print(formatted_string)

# Formatting Numbers

pi = 3.14159
formatted_string = "The value of pi to two decimal places is {:.2f}.".format(pi)
print(formatted_string)

# Padding and Aligning Strings

# Right-align text
formatted_string = "{:>10} | {:<10}".format("Item", "Price")
print(formatted_string)

# Adding values
formatted_string = "{:>10} | {:<10}".format("Apple", 1.50)
print(formatted_string)

# Combining Everything

name = "Bob"
age = 25
height = 1.75

formatted_string = "Name: {0}, Age: {1}, Height: {2:.2f} meters".format(name, age, height)
print(formatted_string)

# Summary

name = "Alice"
age = 30
pi = 3.14159

# Basic usage
print("My name is {} and I am {} years old.".format(name, age))

# Positional and keyword arguments
print("The {0} is {1} years old.".format(name, age))
print("My name is {name} and I am {age} years old.".format(name=name, age=age))

# Formatting numbers
print("The value of pi to two decimal places is {:.2f}.".format(pi))

# Padding and aligning
print("{:>10} | {:<10}".format("Item", "Price"))
print("{:>10} | {:<10}".format("Apple", 1.50))

# Combining everything
height = 1.75
print("Name: {0}, Age: {1}, Height: {2:.2f} meters".format(name, age, height))

