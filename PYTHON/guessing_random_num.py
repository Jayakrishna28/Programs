import random
number=random.randint(1,10)
print(number)
n=0
guess=0
while guess != number:
    guess=int(input("guess:"))
    if guess != number:
        print('TRY AGAIN!!!!')
        continue
    else:
        print('GREAT!!!!')
        break