import cmath
a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
d=(b*b)-(4*a*c)
x=(-b+cmath.sqrt(d))/2*a
y=(-b-cmath.sqrt(d))/2*a
print(x)
print(y)