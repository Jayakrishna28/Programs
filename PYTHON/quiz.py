p=0
print("WELCOME TO QUIZ")
print('''1.What is the value of 23+2?
a. 23
b. 25
c. 27
d. 36''')
res_1=input()
if res_1 == "b":
   p+=1
   print("correct!!")
else:
   print("wrong!!")
print('''2.What is the value of 22-3?
a.19
b.33
c.22
d.32''')
res_2=input()
if res_2 =="a":
   p+=1
   print('CORRECT!!')
else:
   print('WRONG!!')
print("Your Score:",p,"\2")