# Calculate a person's BMI from height and weight
# Week 2 

# Veronica Curry
# Student ID: G00074924


# details given by Andrew to input:
# weight 65kg / height 180cm 
# Result - 20.06

# Methodology
# Get formula for BMI
# Set inputs
# Pass inputs through formula
# set correct number types and measurement types

name = input ('Enter your name: ')                                          # 1. Set variable "name" - which is the input from "Enter your Name
print('Hello ' + name + '\nNice to meet you, lets calculate your BMI!')     # 2. Print Statement - Hello "name" / New line  /- nice to meet you, lets calculate your BMI!

height = float(input('Enter your height in CM: '))                          # 3. Set variable "height" - Input set as an interger ( set as a number to allow for arithemetic)
heightinmeters = height / 100                                               # 4. Set variable "heightinmetres" - this is height divided by 100 - cm changed to metres
print('Your height in meters is {}'.format(heightinmeters))                 # 5. Print statement telling user height in cm / using format to add hightinmetres into statement - allows for changes/ variables

weight = float(input("Input your weight in Kilogram: "))                    # 6. Set variable "Weight" - Input set as an interger ( set as a number to allow for arithemetic)
print('Your weight is {}'.format(weight))                                   # 7. Print statement telling user weight / using format to add weight into statement

BMI = (round(weight / (heightinmeters * heightinmeters), 2))                # 8. Calculate BMI - round the result of weight divded by heightinmetres squared
print ( " Your BMI is {}".format (BMI))                                     # 9. Print statement Your BMI is - using format to input the variable of the BMI result



# Reference 1 - http://www.kingsweightlossclinics.co.uk/resources/bmi-checker/
# Reference 2 - https://stackoverflow.com/questions/20405610/bmi-calculator-in-python/50386292#:~:text=')%20while%20input%20%3D%3D%20'imperial,which%20means%20you%20are%20underweight.
# Reference 3 - https://codereview.stackexchange.com/questions/217751/simple-bmi-calculator-python-3
# Reference 4 - https://www.slimmingworld.ie/bmi-calculator
