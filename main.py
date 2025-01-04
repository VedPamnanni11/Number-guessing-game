import random

pickedNum = random.randint(1, 100)
guessedNum = 0
tries = 0

while guessedNum != pickedNum:
    try:
        guessedNum = int(input("Guess a number between 1-100 : "))
        if guessedNum < 1 or guessedNum > 100:
            print("Please enter a number between 1 and 100!")
            
        tries += 1

        if guessedNum < pickedNum:
            print("BIGGER!")
        
        elif guessedNum > pickedNum:
            print("smaller!")

    except ValueError:
        print("Please enter a valid number!")

print(f"Congrats you have guessed the number in {tries} tries.")        