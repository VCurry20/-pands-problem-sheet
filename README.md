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

This code asks the user to input their name and greets them. The user is then asked for their height and weight and from this the program calculates their BMI. BMI formula (weight / (height * height), 2)


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

This code asks the user for an input - example " The quick brown fox jumps over the lazy dog." . The program reverts this input and returns the sentence missing every second letter - example output ".o zletrv pu o wr cu h". This program uses slicing and also reversing.


References:

- Youtube, Python Tutorial: Slicing lists and Strings (Oct 29, 2015) - https://www.youtube.com/watch?v=ajrtAuDg3yw (Accessed: February 2021)

- W3 Schools, How to reverse a string, (No Date) - https://www.w3schools.com/python/python_howto_reverse_string.asp (Accessed: February 2021)

- Salty Crane Blog, How to reverse words in a sentence using Python and C (April 22, 2009) - https://www.saltycrane.com/blog/2009/04/how-reverse-words-sentence-using-python-and-c/ (Accessed: February 2021)
<br/>

# Task 3  - Collatz


> File - [collatz.py](https://github.com/VCurry20/-pands-problem-sheet/blob/main/collatz.py)

> Objective - Write a program that asks users to input a positive integer and outputs a list of successive values - successive values calculated as follows - if even divide by two, if odd multiply by three and add one. Program stops at zero.

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

# Task 4  - Weekday


> File - [weekday.py](https://github.com/andrewbeattycourseware/pands-problems/blob/master/weekday.py)

> Objective - Write a program that outputs whether today is a weekday or not.

> Input - Any day of the week - for example Monday

> Output - For the weekdays; " Yes, unfortunately today is a weekday.", for the Weekend days; " It is the Weekend, Yay!".


## Code:

```ruby
import datetime                                                                           
weeknumber = datetime.datetime.today().weekday()

week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday","Saturday","Sunday")      


def whichdayisit (weekday):                                                               
    
    for weekday in range (0,4):                                                           
        return ("Yes, unfortunately it's a weekday")                                      

    else:                                                                                 
        for weekday in range (5,6):                                                                               
            return ("It is the weekend, yay!")                                            


day = input ("Please enter a day of the week: ")                                          
print (whichdayisit (day))                                                                
```
In this program the user is asked to input a day and it returns if it is a weekend or not. The program workds from a predefined formula, which uses the imported datetime module.


References:

- Pythonic.com, Weekday Function in Python (2020) - https://pythontic.com/datetime/date/weekday (Accessed: March 2021)
- Stack Overflow, How to find current day is weekday or weekends in Python? Duplicate, (2015) - https://stackoverflow.com/questions/29384696/how-to-find-current-day-is-weekday-or-weekends-in-python (Accessed: March 2021)
- Docs.python.org, date.weekday function, datetime- Basic data and time types (No Date) - https://www.saltycrane.com/blog/2009/04/how-reverse-words-sentence-using-python-and-c/ (Accessed: March 2021)
- Github Gist, Python Weekend Checker (2015) - https://gist.github.com/patrickbeeson/e7e848e3398f287c86ea (Accessed: March 2021)
- Youtube, Python:datetime.date (2016) - https://www.youtube.com/watch?v=nLaq7phtsUU (Accessed: March 2021)
- Realpython, The Python return statement: usage and best practices (2020) - https://realpython.com/python-return-statement/ (Accessed: March 2021)


<br/>


# Task 5 - Square Root


> File - [Squareroot.py](https://github.com/VCurry20/-pands-problem-sheet/blob/main/squareroot.py)

> Objective - Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.

> Input - 14.5

> Output - 3.8


## Code:

```ruby
def squareRoot (number):                 
    x=float(number)                      
    y=1.000000                           
    e=0.000001                           
    while x - y > e:                     
          x = (x + y) / 2                
          y = number/x                   
    print (round(x,2))                   

number = input('enter the number : ')    
squareRoot (float(number))               
```

.


References:

- Youtube, Square root of any number instantly - shortcut math (May 6th, 2016) - https://www.youtube.com/watch?v=PJHtqMjrStk (Accessed: March 2021)

- GeeksforGeeks.org, Find root of a number using Newton’s method (May 18th, 2020) - https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/#:~:text=Let%20N%20be%20any%20number,correct%20square%20root%20of%20N. (Accessed: March 2021)

- Stack Overflow, Square root without pre-defined function in python (2018) - https://stackoverflow.com/questions/46183020/square-root-without-pre-defined-function-in-python (Accessed: March 2021)

- Stack Overflow, Limiting floats to two decimal points (2009) - (https://stackoverflow.com/questions/455612/limiting-floats-to-two-decimal-points) a number using Newton’s method (May 18th, 2020) - https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/#:~:text=Let%20N%20be%20any%20number,correct%20square%20root%20of%20N. (Accessed: March 2021)

<br/>


# Task 6  - 


> File - [es.py](https://github.com/VCurry20/-pands-problem-sheet/blob/main/es.py)

> Objective - Write a program that reads in a TXT file and output the number of "e"'s it contains

> Input - Ulysses by James Joyce

> Output - 141150


## Code:

```ruby
import sys                         

with open (sys.argv[1]) as f:       
    data = f.read()                 
    freq = data.count("e")          
    print (freq)                   


## Run file by python typing >  es.py Ulysses.txt  < the in command line ##
```
This program uses the imported System module to access outside files, it then accesses a txt document containing Ulysses by James Joyce. The txt.file is reviewed for "e"'s and the number of "e"'s is returned to the user.

References:

- Gutenberg.org, The Project Gutenberg eBook of Ulysses, by James Joyce (Dec 27, 2019) - https://www.gutenberg.org/files/4300/4300-0.txt (Accessed: April 2021)

- Stack Overflow, Counting specific letters or symbols in a text file in Python (2014) - https://stackoverflow.com/questions/22694244/counting-specific-letters-or-symbols-in-a-text-file-in-python (Accessed: April 2021)

- Python Examples, Python – Count Number of Characters in Text File (No Date) - https://pythonexamples.org/python-count-number-of-characters-in-text-file/ (Accessed: April 2021)

- Geeks for Geeks, Count the number of times a letter appears in a text file in Python (Nov 25, 2020)   https://www.geeksforgeeks.org/count-the-number-of-times-a-letter-appears-in-a-text-file-in-python/ (Accessed: April 2021)

- Tutorialspoint, Python - Command line arguments (No Date) - https://www.tutorialspoint.com/python/python_command_line_arguments.htm (Accessed: April 2021)

- Python Docs, System Specific Parameters and Functions (No Date) - https://docs.python.org/3/library/sys.html (Accessed: April 2021)

<br/>


# Task 7  - 


> File - [secondstring.py](https://github.com/VCurry20/-pands-problem-sheet/blob/main/secondstring.py)

> Objective - 

> Input - 

> Output - 


## Code:

```ruby
phrase = input ( "Please submit a phrase: ")                                            
print ( "Your phrase is: " + phrase +"\nWe will now return this reverted")              

print ( "Your phrase reverted is: " + (phrase[::-1]))                                  

print ( "Your phrase revert and missing every second letter is: " + (phrase[::-2]))
```

.


References:

- Youtube, Python Tutorial: Slicing lists and Strings (Oct 29, 2015) - https://www.youtube.com/watch?v=ajrtAuDg3yw (Accessed: February 2021)

- W3 Schools, How to reverse a string, (No Date) - https://www.w3schools.com/python/python_howto_reverse_string.asp (Accessed: February 2021)

- Salty Crane Blog, How to reverse words in a sentence using Python and C (April 22, 2009) - https://www.saltycrane.com/blog/2009/04/how-reverse-words-sentence-using-python-and-c/ (Accessed: February 2021)

<br/>
