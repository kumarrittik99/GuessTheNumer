import random
randomNumber=random.randint(1,10)
while(1):
   enteredNumber=int(input("Guess and enter a random number between 1 to 10\n"))
   if(enteredNumber>randomNumber):
       print("Guess something lower than this!")
   elif(enteredNumber<randomNumber):
       print("Guess something higher!")
   else:
       print("Bingo!!! You guessed it right!")
       exit(0)