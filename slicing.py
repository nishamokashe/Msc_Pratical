text = "Hello, World!"

# Basic slicing
print(text[0:5])      # Hello
print(text[7:12])     # World

# Omitting indices
print(text[:5])       # Hello
print(text[7:])       # World!

# Negative indices
print(text[-6:-1])    # World
print(text[-1])       # !

# Slicing with step
print(text[::2])      # Hlo ol!
print(text[0:10:2])   # Hlo ol

# Reversing a string
print(text[::-1])     # !dlroW ,olleH
