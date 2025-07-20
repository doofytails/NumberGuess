import random

MIN_NUM = 1
MAX_NUM = 100
ANSWER = 0
is_game_on = True
GUESSES = 0

ANSWER = random.randint(MIN_NUM, MAX_NUM)



print(f"Guess a number between {MIN_NUM} to {MAX_NUM}")

intguess = int(input("Your guess: "))

while is_game_on:

    if intguess > ANSWER:
        print("Too high, try again!")
        GUESSES += 1
        intguess = int(input("Your guess: "))

    elif intguess < ANSWER:
        print("Too low, try again!")
        GUESSES += 1
        intguess = int(input("Your guess: "))


    elif intguess == ANSWER:
        print("You did it!")
        print(f"You had {GUESSES} guesses!")
        print("Would you like to try again?")
        resume = input("Enter Y to resume or N to quit: ").upper()
        if resume == ("Y"):
            intguess = int(input("Your guess: "))
            
        elif resume == ("N"):
            print("See you again later!")
            is_game_on = False