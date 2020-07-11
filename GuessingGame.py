from random import randint

for x in range(1,7):
    guessNumber = int(input("Enter Guess Number(1 to 6): "))
    randomNumber = randint(1,6)

    if guessNumber == randomNumber:

        print("Won")
    else:
         print("Lost")
    print("Random Number: ",randomNumber)