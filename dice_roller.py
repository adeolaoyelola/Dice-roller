import random

print("Dice Roller")
roll_count = 0

while True:
    input("Press Enter to roll the dice...")
    dice = random.randint(1,6)
    rollcount += 1

    print("You rolled:", dice)
    print("Number of rolls:", roll_count)

    again = input("Would you like to roll again? (yes/no): ")

    if again.lower() != "yes":
        print("You rolled the dice:", roll_count)
        print("Thanks for playing!")
        break