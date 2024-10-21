''' Develop a Calculator class with following mathematical operations:
addition, subtraction, multiplication, division, maximum, minimum. '''

class Calculator:
    
    # Method for addition
    def add(self, a, b):  #self: This parameter refers to the instance of the class. 
	                             
        return a + b
    
    # Method for subtraction
    def subtract(self, a, b):
        return a - b
    
    # Method for multiplication
    def multiply(self, a, b):
        return a * b
    
    # Method for division 
    def divide(self, a, b):
        if b == 0:
            return "Error! Division by zero."
        else:
            return a / b
    
    # Method to find the maximum of two numbers
    def maximum(self, a, b):
        return max(a, b)
    
    # Method to find the minimum of two numbers
    def minimum(self, a, b):
        return min(a, b)

# Example usage
calc = Calculator()

# Performing operations
a, b = 10, 5

print(f"Addition of {a} and {b}: {calc.add(a, b)}")
print(f"Subtraction of {a} and {b}: {calc.subtract(a, b)}")
print(f"Multiplication of {a} and {b}: {calc.multiply(a, b)}")
print(f"Division of {a} and {b}: {calc.divide(a, b)}")
print(f"Maximum of {a} and {b}: {calc.maximum(a, b)}")
print(f"Minimum of {a} and {b}: {calc.minimum(a, b)}")
