# Write a program asks for input - integer; successive outputs dependent on even or odd - program stops at 1
# Calculate each step - if int even - divide by two
# else if if is odd muliply by three and add one
# Program end at 1

# Week 4
# Task 4

# Veronica Curry
# Student ID: G00074924


# Answer - 
# Please enter a positive integer:  10
# result: 10, 5, 16, 8, 4, 2, 1


"""# Methodology:
# required - while loop - stops when hits a value - set in program
# need to set loop parameters - stop when hits 1
# evaluate even vs odd - boolean - true / falue -- % = 0 
# set commands for even and odd - even / 2  - odd * 3 + 1
# lists [] values - append 
# set formula """


def formula (number):                                           # 1. Define Formula
    if (number % 2) == 0:                                       # 2. Check if even - modulus % 2 - if when divided down by 2 the result is 0 its even
        return int(number / 2)                                  # 3. If even - return the number -  divide the number by 2
   
    else:                                                       # 4. If False / else ( if it does not fulfill (number % 2) == 0: it is automatically false )
        return int( (number * 3) + 1)                           # 5. Then return ( number multiplied by 3, minus 1)


number = int (input("Please enter a positive integer:"))        # 6. Set the variable as input - that input is set as an interger

print(number)                                                   # 7. Print number ( this is the input number e.g 10)
while(number !=1):                                              # 8. While value is set for the formula to run - while number is not equal to 1
        number = formula (number)                               # 9. New number - which is (number) run through the formula
        print (number)                                          # 10. Print Number 

print(number)                                                   # 11. Print the output of number run through the formula - i.e the result




# Reference 1. https://stackoverflow.com/questions/39835536/python-multiplying-all-even-numbers-in-a-list
# Reference 2. https://pythonprogramming.net/if-statement-python-3-basics-tutorial/
# Reference 3. https://dev.to/vikkyomkar/3-ways-to-find-if-a-number-is-odd-even-in-python-1ao7
# Reference 4. https://www.youtube.com/watch?v=lAp_5qTdOhM
# Reference 5. https://stackoverflow.com/questions/33508034/making-a-collatz-program-automate-the-boring-stuff
