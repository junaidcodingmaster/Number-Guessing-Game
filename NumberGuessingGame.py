import random
import pyfiglet
from simple_chalk import chalk
import os
from JunaidCredit import *

# On Start
os.system("cls")

## style varables
header = chalk.blue.bold("_____________________")
rawLogo = pyfiglet.figlet_format("Number Guessing Game")
logo = chalk.blue.bold(rawLogo)
rawWon = pyfiglet.figlet_format("YOU WON!")
rawLose = pyfiglet.figlet_format("YOU LOSE!")
won = chalk.green.bold(rawWon)
lose = chalk.red.bold(rawLose)

# main varables
ranNum = random.randint(1, 9)
chances = 0


# Display

# Header
print(logo)
print(header)

print("\n")

print("Guess a number between 1 to 9.")


# functions

while chances < 5:

    # Enter a number between 1 to 9

    try:
        guess = int(input("Enter your guess:- "))
    except KeyboardInterrupt:
        JunaidCredit.error(1)
    except ValueError:
        JunaidCredit.error(2)
    else:
        pass

    # Compare the user entered number with the number to be guessed

    if guess == ranNum:

        print(won)
        print(chalk.green("Congratulation YOU WON!!!"))
        JunaidCredit.main()
        break

    # Check if the user entered ranNum is smaller than the generated ranNum
    elif guess < ranNum:
        print("Your guess was too low: Guess a number higher than", guess)

    # The user entered number is greater than the generated number
    else:
        print("Your guess was too high: Guess a number lower than", guess)

    # Increase the value of chance by 1
    chances = chances + 1


# Check whether the user guessed the correct number
if not chances < 5:

    print(lose)
    print(chalk.red("YOU LOSE!!! The number is"), ranNum)
    JunaidCredit.main(0)



