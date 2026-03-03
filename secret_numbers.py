import random

random_number = random.randint(1, 20)
attempts = 5

for i in range(attempts):
    number = int(input("Attempt " + str(i+1) + ": Guess the number between 1 and 20 "))
    if number == random_number:
        print("You guessed the number!")
        break
    elif number < random_number:
        print("Too low!")
    else:
        print("Too high!")

if number != random_number:
    print("You've used all your attempts. The number was " + str(random_number))