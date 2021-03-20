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


import weekday

weekdays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
 
def whichdayisit (weekday):
    
    if weekdays in range (0,4):
        return ("Yes, unfortunately it's a weekday")

    else:
        return ("It is the weekend, yay!")


day = input ("Please enter a day of the week: ")  
print (whichdayisit (day))

         

# Reference 1: https://pythontic.com/datetime/date/weekday
# Reference 2: https://stackoverflow.com/questions/29384696/how-to-find-current-day-is-weekday-or-weekends-in-python
# Reference 3: https://docs.python.org/3/library/datetime.html#datetime.date.weekday
# Reference 4: https://gist.github.com/patrickbeeson/e7e848e3398f287c86ea
# Reference 5: https://www.youtube.com/watch?v=nLaq7phtsUU
# Reference 6: https://realpython.com/python-return-statement/