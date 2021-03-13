# Calculate a perons BMI from Height and weight
# Week 2 
# Task 1

# Veronica Curry
# Student ID: G00074924


# details given by Andrew to input:
# weight 65kg / height 180cm 
# Result - 20.06


name = input ('Enter your name: ')
print('Hello ' + name + '\nNice to meet you, lets calculate your BMI!')

height = float(input('Enter your height in CM: '))
heightinmeters = height / 100

print('Your height in meters is {}'.format(heightinmeters))

weight = int(input("Input your weight in Kilogram: "))

print('Your weight is {}'.format(weight))

BMI = (round(weight / (heightinmeters * heightinmeters), 2))
print ( " Your BMI is {}".format (BMI))



# Ask for details and put details in to formula
# inputs - change CM to M - Formula
# Present clear questions / calculate / give BMI


# Reference 1 - BMI formula http://www.kingsweightlossclinics.co.uk/resources/bmi-checker/
# Reference 2 - BMI Python https://stackoverflow.com/questions/20405610/bmi-calculator-in-python/50386292#:~:text=')%20while%20input%20%3D%3D%20'imperial,which%20means%20you%20are%20underweight.
