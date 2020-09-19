import random

print('Hello, what is your name?')
userName = input()

print('Well ' + userName + ', I am thinking about a number between 1 and 20, please take a guess')
myNumber = random.randint(1, 20)

for i in range (1, 7):
    guessNumber = int(input())
    if guessNumber > myNumber:
        print('This is too high')
    elif guessNumber < myNumber:
        print('This is too low')
    else:
        break #The number is guessed correctly

if (guessNumber == myNumber):
    print('Your guess is correct, good job! you took ' + str(i) + ' guesses')
else:
    print('You could not guess my number, it was ' + str(myNumber))
    
