# -pands-problem-sheet

# Weekly Tasks for PANDS 2021 
Author Veronica Curry

Student ID: G00074924

This file contains the overview for the 7 weekly tasks for the Programing and Scripting Module, GMIT, 2021.


<br/>
<br/>


# Task 1  - BMI


> File - [BMI.py](https://github.com/VCurry20/-pands-problem-sheet/blob/main/BMI.py)

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

- Kings Weightloss Clinic, BMI Checker, (No Date), http://www.kingsweightlossclinics.co.uk/resources/bmi-checker/ (Accessed: February 2021)

- Stack Overflow, BMI Calculator Python, (2014), https://stackoverflow.com/questions/20405610/bmi-calculator-in-python/50386292#:~:text=')%20while%20input%20%3D%3D%20'imperial,which%20means%20you%20are%20underweight. (Accessed: February 2021)

- W3 Resource, BMI Python Forumla (2017), https://www.w3resource.com/python-exercises/python-basic-exercise-66.php (Accessed: February 2021)

- Slimming World, BMI Calculator, (No Date) https://www.slimmingworld.ie/bmi-calculator (Accessed: February 2021)


<br/>

# Task 2  - Second String


> File - [secondstring.py](https://github.com/VCurry20/-pands-problem-sheet/blob/main/secondstring.py)

> Objective - Write a program that asks for a input and outputs every second letter in reverse

> Input - The quick brown fox jumps over the lazy dog.

> Output - .o zletrv pu o wr cu h


## Code:

```ruby
phrase = input ( "Please submit a phrase: ")                                            
print ( "Your phrase is: " + phrase +"\nWe will now return this reverted")              

print ( "Your phrase reverted is: " + (phrase[::-1]))                                  

print ( "Your phrase revert and missing every second letter is: " + (phrase[::-2]))
```

This code asks the user for an input - example " The quick brown fox jumps over the lazy dog." . The program reverts this input and returns the sentence missing every second letter - example output ".o zletrv pu o wr cu h". This program uses slicing.


References:

- Youtube, Python Tutorial: Slicing lists and Strings (Oct 29, 2015) - https://www.youtube.com/watch?v=ajrtAuDg3yw (Accessed: February 2021)

- W3 Schools, How to reverse a string, (No Date) - https://www.w3schools.com/python/python_howto_reverse_string.asp (Accessed: February 2021)

- Salty Crane Blog, How to reverse words in a sentence using Python and C (April 22, 2009) - https://www.saltycrane.com/blog/2009/04/how-reverse-words-sentence-using-python-and-c/ (Accessed: February 2021)
<br/>

# Task 3  - Collatz


> File - [collatz.py](https://github.com/VCurry20/-pands-problem-sheet/blob/main/collatz.py)

> Objective - Asks users to input a positive integer and outputs a list of successive values - successive values calculated as follows - if even divide by two, if odd multiply by three and add one. Program stops at zero.

> Input - 10

> Output - 10,5,16,8,4,2,1


## Code:

```ruby
def formula (number):                                           
    if (number % 2) == 0:                                       
        return int(number / 2)                                  
   
    else:                                                       
        return int( (number * 3) + 1)                           


number = int (input("Please enter a positive integer:"))        

print(number)                                                   
while(number !=1):                                              
        number = formula (number)                               
        print (number)                                          

print(number)                                                   
```
In this program a formula is definied; this checks if the number is even - if even it divides by 2, if not it is odd and therefore it is multiplied by 3 and 1 is added to it.
From this formula numbers are then passed through - each number is printed to the variable and returned as an output at the end of the program.

References:

- Stack Overflow, Python Multiplying all even numbers in a list (2017) - https://stackoverflow.com/questions/39835536/python-multiplying-all-even-numbers-in-a-list (Accessed: February 2021)
- Python Programming.net, If statments python tutorial ( Jan 13th, 2014) - https://pythonprogramming.net/if-statement-python-3-basics-tutorial/ (Accessed: February 2021)
- Dev Community, 3 wats to find if a numbers is odd/even in python ( Aug 27th, 2020) - https://dev.to/vikkyomkar/3-ways-to-find-if-a-number-is-odd-even-in-python-1ao7 (Accessed: February 2021) 
- Youtube, Collatz Sequence Algorithm in Python! ( May 8, 2020) - https://www.youtube.com/watch?v=lAp_5qTdOhM (Accessed: February 2021)
- Stack overflow - Making a collatz program automate the boring stuff (2016) -https://stackoverflow.com/questions/33508034/making-a-collatz-program-automate-the-boring-stuff (Accessed: February 2021)
- Automate the boring stuff, Al Sweigart, - Collatz - pg 77 - http://files.urpdfs.com/automate-the-boring-stuff-with-python.pdf (Accessed: February 2021)



<br/>