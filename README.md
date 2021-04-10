# -pands-problem-sheet

# Weekly Tasks for PANDS 2021 
Author Veronica Curry

Student ID: G00074924

This file contains the overview for the 7 weekly tasks for the Programing and Scripting Module, GMIT, 2021.


<br/>
<br/>


<<<<<<< HEAD
## Task 1  - BMI


> File Name - BMI.py - (./BMI.py)
=======
## Task 1 BMI


> File Name - BMI.py 
>>>>>>> ae4eb589f6a5904c263cb4815f4aa0cb8ca2e153

> Objective - Write a program that calculates a person's BMI

> Input - Person's height in Centimetres and weight in Kilograms

> Output - BMI - weight divided by height in metres SQ


<br/>
<br/>

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

