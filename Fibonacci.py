''' Write a program to Fibonacci series in python. '''

n=int(input("Enter the value of the term : "))
a = 0
b = 1
c = 0
count = 1
print("Fibonacci Series: ", end = " ")
while(count <= n):
    print(c, end = " ")
    count += 1
    a = b
    b = c
    c = a+b