x=input('x=')
y=input('y=')
temp=x
x=y
y=temp
print(x)
print(y)
# Multiplication table (from 1 to 10) in Python

num = 12

# To take input from the user
# num = int(input("Display multiplication table of? "))

# Iterate 10 times from i = 1 to 100
for i in range(1, 101):
   print(num, 'x', i, '=', num*i)
