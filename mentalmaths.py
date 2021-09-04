# imports
import random # for random numbers
import asyncio # for timer and running main function as asynchronous

# rule variable declaration
rule1 = "1.) You select a difficulty, a calculation is generated by the computer, and you have to answer it in the correct amount of time."
rule2 = "2.) If you answer the question in the correct amount of time, you have beaten the computer, and asked if you want to play again."
rule3 = "3.) If you answer the question incorrectly, you haven't beaten the computer, the answer is printed and you are asked if you want to play again."
rule4 = "4.) If you chose to play again, the while loop will reset."
rule5 = "5.) If you don't want to play again, the loop is ended and the program is exited."

# operators list
operators = ["-", "+"]

# main function
async def main():
    # menu boolean declaration
    menu = True 
    # print statement
    print("would you like to play a game? yes or no? ")
    # userinput
    gameInput = input()
    # if 
    if gameInput == "yes":
        # while loop
        while menu:
            # variables to declare
            rules = f"{rule1}\n{rule2}\n{rule3}\n{rule4}\n{rule5}"
            # print statement (rules)
            print(rules)
            print("the computer will now think of a caluculation: ")
            # variables to declare
            number1 = random.randint(1,100) 
            number2 = random.randint(1,100)
            operator = random.choice(operators)
            # if
            if operator == "+":
            # variables to declare
                answer = number1+number2
            # elif
            elif operator == "-":
                # variables to declare
                answer = number1-number2 
            # variables to declare
            calculation = f"Calculation: {number1} {operator} {number2}"
            # print statement
            print("are you ready to work out the calculation? yes or no? ")
            # user input
            workoutInput = str(input())
            # if
            if workoutInput == "yes":
                # variables to declare
                difficultyInput = input("what would you like your difficulty to be? easy, medium, or hard? ")
                # print statement (calculation)
                print(calculation)
                # if
                if difficultyInput == "easy":
                    # variable declaration 
                    n = 0
                    # for loop
                    for n in range (0, 9):
                        # print statement (n)
                        print(n)
                        # waits for 1 second 
                        await asyncio.sleep(1)
                        # changes value of n by 1 at the end of each loop
                        n = n + 1 
                # elif
                elif difficultyInput == "medium":
                    # variable declaration
                    n = 0
                    # for loop
                    for n in range (0, 7):
                        # print statement (n)
                        print(n)
                        # waits for 1 second
                        await asyncio.sleep(1)
                        # changes value of n by 1 at the end of each loop
                        n = n + 1              
                # elif
                elif difficultyInput == "hard":
                    # variable declaration
                    n = 0
                    # for loop
                    for n in range (0, 5):
                        # print statement
                        print(n)
                        # waits for 1 second
                        await asyncio.sleep(1)
                        # changes value of n by 1 at the end of each loop
                        n = n + 1
                # print statement
                print("time is up!\nwhat is your answer? ")
                # user input
                useranswer = int(input()) 
                # if
                if useranswer == answer:
                    # print statement
                    print("correct! well done!")
                # else
                else: 
                    # print statement
                    print(f"incorrect! the answer was: {answer}")
                # print statement
                print("would you like to play again? yes or no? ")
                # user input
                againInput = str(input())
                # if
                if againInput == "no":
                    # print statement
                    print("exitting program!")
                    # menu boolean declaration
                    menu = False
            # else
            else:
                # print statement
                print("exiting program!")
                # menu boolean declaration
                menu = False 
    # else
    else:
        # print statement
        print("exiting program!")

# running main function
asyncio.run(main())