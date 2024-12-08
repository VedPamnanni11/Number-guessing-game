import random

allNums = list(range(1, 101))
pickedNum = random.choice(allNums)
guessedNum = int(input('Guess a number : '))
while True:
    while True:
        if pickedNum == guessedNum:
            print('You won!')
            
        
        elif pickedNum >= guessedNum:
            print('BIGGER!')
            guessedNum = int(input('Guess a number : '))
            break
        
        elif pickedNum <= guessedNum:
            print('smaller!')
            guessedNum = int(input('Guess a number : '))
            break
        
        else:
            print('error')
            break