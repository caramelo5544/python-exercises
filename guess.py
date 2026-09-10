import random

secret = random.randint(1, 20)
tries = 0

while True:
    guess = int(input("Guess (1-20): "))
    tries = tries + 1
    if guess < secret:
        print("Higher!")
    elif guess > secret:
        print("Lower!")
    else:
        print("Correct! Tries:", tries)
        f = open("scores.txt", "a")
        f.write(str(tries) + "\n")
        f.close()
        break