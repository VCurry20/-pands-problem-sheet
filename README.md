# -pands-problem-sheet

# Weekly Tasks for PANDS 2021 
Author Veronica Curry

Student ID: G00074924

This file contains the overview for the 7 weekly tasks for the Programing and Scripting Module, GMIT, 2021.


<br/>
<br/>


# Task 1  - BMI


> File - [BMI.py](./https://github.com/VCurry20/-pands-problem-sheet/blob/main/BMI.py)

> Objective - Write a program that calculates a person's BMI

> Input - Person's height in Centimetres and weight in Kilograms

> Output - BMI - weight divided by height in metres SQ


## Code:

```ruby
name = input ('Enter your name: ')                                          
print('Hello ' + name + '\nNice to meet you, lets calculate your BMI!')     

height = float(input('Enter your height in CM: '))                          
heightinmeters = height / 100                                              
print('Your height in meters is {}'.format(heightinmeters))                 

weight = float(input("Input your weight in Kilogram: "))                    
print('Your weight is {}'.format(weight))                                   

BMI = (round(weight / (heightinmeters * heightinmeters), 2))                
print ( " Your BMI is {}".format (BMI)) 
```

This code asks the user to input their name and greets them. The user is then asked for the height and weight and from this the program calculates their BMI.

References:

- BMI formula (http://www.kingsweightlossclinics.co.uk/resources/bmi-checker/)

- BMI Python (https://stackoverflow.com/questions/20405610/bmi-calculator-in-python/50386292#:~:text=')%20while%20input%20%3D%3D%20'imperial,which%20means%20you%20are%20underweight.)

- BMI Python Forumla (https://www.w3resource.com/python-exercises/python-basic-exercise-66.php)

- BMI Calculator (https://www.slimmingworld.ie/bmi-calculator)