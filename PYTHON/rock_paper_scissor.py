#r>s s>p p>r
import random
your_score=0
sys_score=0
no_of_games=5
n=0
while n<no_of_games+1:
    sys=random.choice(['r','p','s'])
    choice=input('Enter your choice:\ns-scissor r-rock p-paper')
    if choice == sys:
        print('tie')
    elif (choice == 'r' and sys == 's') or (choice == 's' and sys == 'p') or (choice =='p' and sys =='r'):
        print('you won')
        your_score += 1
    else:
        print('try again')
        sys_score += 1
    n +=1
print(f'your score:{your_score}\nsys score:{sys_score}')
if your_score > sys_score:
    print('YAYYY You Won')
else:
    print('You lose')