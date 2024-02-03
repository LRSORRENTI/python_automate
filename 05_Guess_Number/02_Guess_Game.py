import random


def Guess_Game():
    print('You have 6 guesses to guess the secret number which is a number between 1 and 20, enter a number')
    try:
        num = int(random.randint(1, 20))
        numGuesses = 0
        for numGuesses in range (0, 6):
            userGuess = input()
            userGuess = int(userGuess)  # Convert input to integer once and use it multiple times
            if numGuesses >= 5:
                print('It took more than 6 guesses, sorry the number was:', num)
                return
            if userGuess == num:
                print('You win congrats! The number was', num, 'and it took you', numGuesses + 1, 'guesses')
                return
            elif userGuess < num:
                print('You guessed too low, guess again')
                numGuesses + 1
            elif userGuess > num:
                print("You guessed too high, guess again")
                numGuesses + 1
    except ValueError:
        print('You did not enter a number')
   
   
Guess_Game()
