# Write a program that outputs whether or not today is a weekday with an associated message

# Week 5
# Task 5

# Veronica Curry
# Student ID: G00074924


# Answer - 
# Please enter a day of the week
# Answer - "Yes, unfortunately its a weekday" or "It is the weekend, yay!" 


# Methodology
## For loops and list of days of the week
## Array / list of days?

# daysofWeek = (Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday)
# weekend = last two of this list - 5, 6

# if when x do a and if not do b


import datetime                                                                           #1. Import datetime module

weekdays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday") #2. Set weekdays
 
def whichdayisit (weekday):                                                               #3. Define formula
    
    for weekday in range (0,4):                                                           #4. For days in range 0 - 4 (Monday - Friday)
        return ("Yes, unfortunately it's a weekday")                                      #5. Print "Unfortunately its the weekday"

    else:                                                                                 #6. Else / Otherwise 
        return ("It is the weekend, yay!")                                                #7. Print "Yay its the weekend"


day = input ("Please enter a day of the week: ")                                          #8. Day is set as input from "please enter a day"
print (whichdayisit (day))                                                                #9. Print the outcome of the input through the formula

         

# Reference 1: https://pythontic.com/datetime/date/weekday
# Reference 2: https://stackoverflow.com/questions/29384696/how-to-find-current-day-is-weekday-or-weekends-in-python
# Reference 3: https://docs.python.org/3/library/datetime.html#datetime.date.weekday
# Reference 4: https://gist.github.com/patrickbeeson/e7e848e3398f287c86ea
# Reference 5: https://www.youtube.com/watch?v=nLaq7phtsUU
# Reference 6: https://realpython.com/python-return-statement/