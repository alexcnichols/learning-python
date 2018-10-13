import random
number = random.randint(1,20)
guess = int(input("I'm thinking of a number from 1 to 20. What is it?"))
while guess != number:
    if guess < number:
        print("Your number was too low...")
    else:
        print("Your number was too high...")
    guess = int(input("Please try again..."))
print("Congratulations! Correct answer!")