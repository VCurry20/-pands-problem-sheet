# Write a program that takes a positive floating-point number as input and outputs an approximation of its square root
# You should create your own function

# Week 6

# Veronica Curry
# Student ID: G00074924

# The numbers should look like this:
# Please enter a positive number: 14.5
# The square root of 14.5 is approx. 3.8


# Methodology:
# What is a Sq Root and how do we work it out?
# Sq Root in Python and how it operates
# Newton in Python
# Clear up mistakes in code / amend to suit


def squareRoot (number):                 # 1. Define formula - everything indented under def is included in the forumla
    x=float(number)                      # 2. Start outlining the meaning of the parts of the formula - x = the float version of input n
    y=1.000000                           # 3. iteration initialisation / starting the looping process 
    e=0.000001                           # 4. accuracy after decimal place / e = float 0.00001
    while x - y > e:                     # 5. While loop - while x - y is greater than e ( 0.00001) - stop at 0.00001 - this keeps going until its find the closest answer
          x = (x + y) / 2                # 6. x = x + y divided by 2
          y = number/x                   # 7. y = n divided by x
    print (round(x,2))                   # 8. result from the formula is round x - for 2 decimal points - x to 2 decimal points

number = input('enter the number: ')    # 9. n is the input from the question 'enter the number '
squareRoot (float(number))               # 10. result is the formula acted on n - n is presented as a float

"""""Code from https://stackoverflow.com/questions/46183020/square-root-without-pre-defined-function-in-python""""


# Reference 1: https://www.youtube.com/watch?v=PJHtqMjrStk
# Reference 2: https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/#:~:text=Let%20N%20be%20any%20number,correct%20square%20root%20of%20N.
# Reference 3: https://stackoverflow.com/questions/46183020/square-root-without-pre-defined-function-in-python
# Reference 4: https://stackoverflow.com/questions/455612/limiting-floats-to-two-decimal-points
# Reference 5: https://www.sololearn.com/Discuss/2228331/how-can-we-calculate-square-root-without-using-any-built-in-function-in-python 
# Reference 6: https://stackoverflow.com/questions/19611198/finding-square-root-without-using-sqrt-function