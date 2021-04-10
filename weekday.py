# Write a program that outputs whether or not today is a weekday with an associated message

# Week 5

# Veronica Curry
# Student ID: G00074924


# Answer - 
# Please enter a day of the week
# Answer - "Yes, unfortunately its a weekday" or "It is the weekend, yay!" 


# Methodology
# For loops and list of days of the week
# Array / list of days?
# daysofWeek = (Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday)
# weekend = last two of this list - 5, 6
# if when x do a and if not do b


import datetime                                                                           #1. Import datetime module
weeknumber = datetime.datetime.today().weekday()

week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday","Saturday","Sunday")       #2. Set weekdays


def whichdayisit (weekday):                                                               #3. Define formula
    
    for weekday in range (0,4):                                                           #4. For days in range 0 - 4 (Monday - Friday)
        return ("Yes, unfortunately it's a weekday")                                      #5. Print "Unfortunately its the weekday"

    else:                                                                                 #6. Else / Otherwise 
        for weekday in range (5,6):                                                       #7. For days in range 5 - 6 (Saturday - Sunday)                      
            return ("It is the weekend, yay!")                                            #8. Print "Yay its the weekend"


day = input ("Please enter a day of the week: ")                                          #9. Day is set as input from "please enter a day"
print (whichdayisit (day))                                                                #10. Print the outcome of the input through the formula

         

# Reference 1: https://pythontic.com/datetime/date/weekday
# Reference 2: https://stackoverflow.com/questions/29384696/how-to-find-current-day-is-weekday-or-weekends-in-python
# Reference 3: https://docs.python.org/3/library/datetime.html#datetime.date.weekday
# Reference 4: https://gist.github.com/patrickbeeson/e7e848e3398f287c86ea
# Reference 5: https://www.youtube.com/watch?v=nLaq7phtsUU
# Reference 6: https://www.codespeedy.com/find-the-day-of-week-with-a-given-date-in-python/
