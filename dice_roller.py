import random

print("Dice Roller")

while True:
    input("Press Enter to roll the dice...")

    dice = random.randint(1, 6)

    print("You rolled:", dice)

    again = input("Would you like to roll again? (yes/no): ")

    if again.lower() != "yes":
        print("Thanks for playing!")
        break