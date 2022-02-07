from simple_chalk import chalk
import datetime
import os

date = datetime.datetime.now()
copyRight = "Number Guessing Game Copyright © " + str(date.year) + " Junaid"


class JunaidCredit:
    def main():
        # Giving a line for Credits
        print("\n")
        # Credits
        print("This game is made by Junaid.")
        print(chalk.bgWhite.black(copyRight))
        return

    def error(error):
        # Error Handler
        if error == 1:
            print(chalk.yellow("Exiting Game"))
            
            # Giving a line for Credits
            print("\n")
            # Credits
            print("This game is made by Junaid.")
            print(chalk.bgWhite.black(copyRight))
            
            # exit
            os._exit(error)
        elif (error == 2) :
            print(chalk.yellow("You Entered a incorrect value."))
            print("To retry the game type : python NumberGuessingGame.py")
                        
            # Giving a line for Credits
            print("\n")
            # Credits
            print("This game is made by Junaid.")
            print(chalk.bgWhite.black(copyRight))
            
            os._exit(1)
        else :
            print(chalk.red("Undefined Error."))
            pass
