# Week 4 Task

# Write a program that asks the user to input a positive integer 
# outputs successive values 

# @ each step calculate the next value by taking the current value and if even - divide by 2 / if odd multiple by three and add one

# answer - 
# Please enter a positive integer:  10
# result: 10, 5, 16, 8, 4, 2, 1
# Notes
# required - while loop - stops when hits a value - set in program
# need to set loop parameters - stop when hits 1
# evaluate even vs odd - boolean - true / falue -- % = 0 
# set commands for even and odd - even / 2  - odd * 3 + 1
# lists [] values - append 


# program parts

number = int (input("Please enter a positive integer:"))
numbers = []

# while number != 1:
    numbers.append (number)

# if (number % 2) == 0:
    print (number / 2)
# else:
    print ( (number * 3) + 1)

# print (" The result is {}".format(numbers))
    






# https://stackoverflow.com/questions/39835536/python-multiplying-all-even-numbers-in-a-list
# https://pythonprogramming.net/if-statement-python-3-basics-tutorial/
# 
