import sys
import secrets


def guessingGame():
    snum = secrets.secretNumber()
    print("Im thinking of a secret number. Your guess:")
    while True:
        guess = int(sys.stdin.readline().strip())
        if (guess == snum):
            print("Correct!")
            break
        else:
            print("Wrong: guess again please: ")
            pass
        pass
    sstring = secrets.secretString()
    print("Ok, now I'm thinking of a secret phrase. Your guess: ")
    while True:
        guess = sys.stdin.readline().strip()
        if (guess == sstring):
            print("Great guess! You win!")
            break
        else:
            print("Incorrect. Please try again:")
            pass
        pass
    pass


guessingGame()
