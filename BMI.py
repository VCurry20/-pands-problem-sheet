# Calculate a perons BMI from Height and weight
# Veronica Curry

# Reference 1 - BMI formula http://www.kingsweightlossclinics.co.uk/resources/bmi-checker/
# Reference 2 - BMI Python https://stackoverflow.com/questions/20405610/bmi-calculator-in-python/50386292#:~:text=')%20while%20input%20%3D%3D%20'imperial,which%20means%20you%20are%20underweight.

# Ask for details and put details in to formula
# inputs - change CM to M - Formula
# Present clear questions / calculate / give BMI

# details given by Andrew - weight 65kg / height 180cm / formula w/h**

name = input ('Enter your name: ')
print('Hello' + name + '\nNice to meet you, lets calculate your BMI!')

height = int(input('Enter your height in CM: '))
heightinmeters = height / 100
print('Your height is ' + str(height))
print('Your height in meters is ' + str(heightinmeters))

weight = input ('Enter your weight in KG: ')
print('Your weight is ' + str(weight))

print('Your BMI is your weight divided by height squared')
