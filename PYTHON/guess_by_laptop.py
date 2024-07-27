import random
def guess(x):
    low=1
    high=x
    feedback=""
    while feedback != 'c':
        guess=random.randint(1,x)
        print(f'guess between 1 to {x} is {guess}')
        print('h or l or c')
        feedback=input('feedback:')
        if feedback == 'h':
            guess=guess-1
            continue
        elif feedback=='l':
            guess=guess+1
            continue
        else:
            print("YAYYYY")
            break
guess(10)