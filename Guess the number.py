import random
randomNumber=random.randint(1,10)
while(1):
   enteredNumber=int(input("Guess and enter a random number between 1 to 10\n"))
   if(enteredNumber>randomNumber):
       print("Guess something lower than this!")
   elif(enteredNumber<randomNumber):
       print("Guess something higher!")
   elif(enteredNumber<1 or enteredNumber>10)
       print("Please guess and enter a numberb between 1 to 10)
   else:
       print("Bingo!!! You guessed it right!")
       exit(0)
