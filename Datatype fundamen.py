a,b=15,20
c,d=3.14,5.20
e,f="Hello","Samir"
g,h=True,False
i,j=5+6j,8+6j
msg=" {} is of type {} "
print(msg.format(a,type(a)))
print(msg.format(c,type(c)))
print(msg.format(e,type(e)))
print(msg.format(g,type(g)))
print(msg.format(i,type(i)))

print()

add="Adition of '{}' and '{}' is '{}' "

print(add.format(a,b,a+b))
print(add.format(c,d,c+d))
print(add.format(e,f,e+f))
print(add.format(g,h,g+h))
print(add.format(i,j,i+j))

