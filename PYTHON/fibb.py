num=int(input("Enter number of terms\t"))
a=0
b=1
i=0
print("The Fibonacci Series:")
while i<num:
  print(a)
  i+=1
  c=a+b
  a=b
  b=c