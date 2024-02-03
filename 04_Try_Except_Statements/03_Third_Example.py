def askDogs():
    print('How many dogs do you have?')
    try:
        numDogs = input()
        numDogs = int(numDogs)  # Convert input to integer once and use it multiple times

        if numDogs < 0:
            print('Negative amount of dogs??')
        elif numDogs == 0:
            print("You don't have any dogs")
        elif numDogs == 1:
            print("You've got one dog, very cool")
        elif 1 < numDogs < 4:
            print('You have some dogs, nice')
        elif numDogs >= 4:
            print("That's a lot of dogs!")
        
    except ValueError:
        print('You did not enter a number')

askDogs()
