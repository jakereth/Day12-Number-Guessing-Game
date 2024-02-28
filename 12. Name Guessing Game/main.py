import random
import art 

print(art.logo)
print("I'm thinking of a number between 1 and 100.")

numberOfGuesses = 0
number = random.randint(1,100)

def lose():
    print("You have run out of guesses, you lose!")

def guess(numberOfGuesses):
    while numberOfGuesses > 0:
        userGuess = int(input("Guess a number: "))
        if userGuess == number:
            print("Congratulations you guessed the number and won!")
            break
        if userGuess > number:
            print("Too high\nGuess again.")
            numberOfGuesses -= 1
            if numberOfGuesses == 0:
                lose()
        if userGuess < number:
            print("Too low\nGuess again.")
            numberOfGuesses -= 1
            if numberOfGuesses == 0:
                lose()

def hard():
    numberOfGuesses = 5
    guess(numberOfGuesses)

def easy(): 
    numberOfGuesses = 10
    guess(numberOfGuesses)

def difficultySelection():
    difficulty = input('Choose a difficulty: "easy" or "hard" ').lower()
    if difficulty == 'hard':
        hard()
    elif difficulty == 'easy':
        easy()
    else:
        print("Invalid selection.")

difficultySelection()