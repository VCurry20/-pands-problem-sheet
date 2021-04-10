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


<br/>

# Task 2  - Second String


> File - [secondstring.py](./https://github.com/VCurry20/-pands-problem-sheet/blob/main/secondstring.py)

> Objective - Write a program that asks for a input and outputs every second letter in reverse

> Input - sentence of the users choice

> Output - sentence in reverse - missing every second letter


## Code:

```ruby
phrase = input ( "Please submit a phrase: ")                                            
print ( "Your phrase is: " + phrase +"\nWe will now return this reverted")              

print ( "Your phrase reverted is: " + (phrase[::-1]))                                  

print ( "Your phrase revert and missing every second letter is: " + (phrase[::-2]))
```

This code asks the user for an input - example " The quick brown fox jumps over the lazy dog." . The program reverts this input and returns the sentence missing every second letter - example output ".o zletrv pu o wr cu h"


References:

- Python Tutorial - https://www.youtube.com/watch?v=ajrtAuDg3yw

- W3 Schools - https://www.w3schools.com/python/python_howto_reverse_string.asp

- Slicing Blog - https://www.saltycrane.com/blog/2009/04/how-reverse-words-sentence-using-python-and-c/