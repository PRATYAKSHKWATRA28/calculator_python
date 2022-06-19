#This Program was written by PRATYAKSH KWATRA for the school practical file for Artificial Intelligence Subject and was tweaked for some changes and fixes . 
"""Fixes and Changes --> 
                         08/02/2022 01:34 IST
                         Added Loop to continue or stop the program as and when needed
                         Added loop_continue variable to determine whether loop will be continuing or stopped
                         Added more comments to make program understandable for anyone
                         Added line outputs in between to make the program look better to the user
                         Added an if elif else statement to check whether user wants to use the program again or not
                         Added Zero division error
                         Seperated Zero division error and Invalid input error"""



loop_continue = 0  #Defining loop_continue variable and assigning 0 value to it so that while loop continues and when we want to stop the loop , we can just tweak the value of loop_continue
while loop_continue == 0:  #While loop to check if the loop has to be continues or not and that can be done by tweaking the value of loop_continue . (0 == continue , any other value == stop)
    #Printing the meaning of all 4 operators to inform the user about the functioning of the calculator
    print(" + = Addition")
    print(" - = Subtraction")
    print(" * = Multiplication")
    print(" / = Division")

    #Using the print function to output a line to be used as a spacer for good looks
    print("---------------------------------------------------")

    #Asking the user to input the first number for the operation
    first_number = int(input("Enter 1st Number: "))

    #Asking the user to input the first number for the operation
    second_number = int(input("Enter 2nd Number: "))

    #Asking the user to input his/her choice of operator for the operation
    operator = input("Choose The Operator (+ , - , * , /) : ")

    if second_number == 0 and operator == "/": #Checking for the values to confirm that a zero division is not taking place and if yes then to decline the command
        operator = "Declined" #If the above if statement returns true then we assign a value different than any operator so that it is declined in next loop and is forwarded as else

    #If elif else statement used to determine the operator which the user has chosen and then to use it for the required operation to continue
    if(operator == "+"): #Checking if the chosen operator is +
        result = first_number + second_number  #Running the addition operation on the 2 values input by the user if the above if statement returns true as the answer
    elif(operator == "-"): #Checking if the chosen operator is -
        result = first_number - second_number  #Running the subtraction operation on the 2 values input by the user if the above elif statement returns true as the answer
    elif(operator == "*"): #Checking if the chosen operator is *
        result = first_number * second_number  #Running the multiplication operation on the 2 values input by the user if the above elif statement returns true as the answer
    elif(operator == "/"): #Checking if the chosen operator is /
        result = first_number / second_number  #Running the division operation on the 2 values input by the user if the above elif statement returns true as the answer
    else: #This else statement runs when the operator input by the user is not equal to either of +,-,*,/ or if zero division is being done
        if operator == "Declined": #Checking is Zero division is being done
                print("Attempted Zero Division") #If the above else statement is executed this command shows the user an output of Attempted Zero Division
                result = "Operation Declined" #When the else statement is executed , r is assigned the value of Operation Declined 
        else:
                print("Invalid Operator Chosen ") #If the above else statement is executed this command shows the user an output of Invalid Operator Chosen 
                result = " N.A." #When the else statement is executed , we assign the value of N.A. 

    print("Result : ", result) #This statement outputs the Result of the above calculations

    print("------------------------------------------------------------------")  #Output for a line to give a Clean look to the program 
    Restart = str(input("Do you want to use the Calculator Again (Y/N) ? : ")) #Asking for input if the user wants to use program again or not
    if Restart.upper() == "Y":  #If elif else to check if the user wants to use the program again or not
        loop_continue = 0  #Assigning 0 value to loop_continue so that loop continues
    elif Restart.upper() == "N": #If elif else to check if the user wants to use the program again or not
        loop_continue = 1  #Assigning 1 value to loop_continue so that loop stops
    else: #to check if the input was other than Y or N
        loop_continue = 1 #Assigning 1 value to loop_continue so that loop stops
        print("Invalid Input ! Program Stopped")  #if the value was different than required , it displays invalid input and stops the program
