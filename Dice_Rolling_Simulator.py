import random

def roll_dice(num_of_dice, sides):
    total = 0
    rolls = []
    for _ in range(num_of_dice):
        roll = random.randint(1, sides)
        rolls.append(roll)
        total += roll
    return rolls, total

def main():
    try:
        num_of_dice = int(input("How many dice do you want to roll? "))
        num_of_sides = int(input("How many sides does this dice have? "))

        rolls, total = roll_dice(num_of_dice, num_of_sides)

        print(f"You rolled: {', '.join(str(roll) for roll in rolls)}")
        print(f"Your total is {total}")
    except ValueError:
        print("Please enter a vaild number for number of dice and sides")

if __name__ == "__main__":
    main()
