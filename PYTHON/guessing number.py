secret_number = 9
i = 0
while i < 3:
    num = int(input("Guess:"))
    i += 1
    if num == secret_number :
      print("You are correct!!")
      break
else :
   print("You lose the game")